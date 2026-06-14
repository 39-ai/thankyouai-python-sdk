from __future__ import annotations

import asyncio
import json
import os
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request as URLRequest
from urllib.request import urlopen

from ._utils import (
    DEFAULT_BASE_URL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT_SECONDS,
    build_query,
    create_idempotency_key,
    merge_headers,
    normalize_base_url,
    parse_json_body,
)
from .errors import ThankYouAPIError, ThankYouTimeoutError, build_api_error


@dataclass(frozen=True)
class RequestOptions:
    timeout: float | None = None
    headers: Mapping[str, str] | None = None
    idempotency_key: str | None = None
    max_retries: int | None = None


@dataclass(frozen=True)
class RequestConfig:
    method: str
    path: str
    body: object | None = None
    query: Mapping[str, object | None] | None = None
    auth: bool = True
    idempotent: bool = False
    options: RequestOptions | None = None


@dataclass(frozen=True)
class TransportRequest:
    method: str
    url: str
    headers: Mapping[str, str]
    body: bytes | None
    timeout: float


@dataclass(frozen=True)
class TransportResponse:
    status: int
    headers: Mapping[str, str]
    body: bytes


Transport = Callable[[TransportRequest], Awaitable[TransportResponse]]


class APIClient:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        workspace_id: str | None = None,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = DEFAULT_MAX_RETRIES,
        transport: Transport | None = None,
        default_headers: Mapping[str, str] | None = None,
    ) -> None:
        self._api_key = api_key
        self._base_url = normalize_base_url(base_url)
        self._workspace_id = workspace_id
        self._timeout = timeout
        self._max_retries = max_retries
        self._transport = transport or default_async_transport
        self._default_headers = default_headers

    def _request_context(
        self,
        config: RequestConfig,
    ) -> tuple[str, str | None, str | None, int]:
        options = config.options or RequestOptions()
        max_retries = options.max_retries if options.max_retries is not None else self._max_retries
        method = config.method.upper()
        idempotency_key = options.idempotency_key or (
            create_idempotency_key() if config.idempotent and method == "POST" else None
        )
        auth_api_key = self._resolve_api_key() if config.auth else None
        return method, idempotency_key, auth_api_key, max_retries

    def _build_request(
        self,
        config: RequestConfig,
        method: str,
        idempotency_key: str | None,
        auth_api_key: str | None,
    ) -> TransportRequest:
        options = config.options or RequestOptions()
        timeout = options.timeout if options.timeout is not None else self._timeout
        url = f"{self._base_url}{config.path}{build_query(config.query or {})}"
        headers = merge_headers(self._default_headers, options.headers)
        if config.auth:
            headers["Authorization"] = f"Bearer {auth_api_key}"
        if self._workspace_id and "x-workspace-id" not in {key.lower() for key in headers}:
            headers["x-workspace-id"] = self._workspace_id
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key

        body_bytes: bytes | None = None
        if config.body is not None:
            headers.setdefault("Content-Type", "application/json")
            body_bytes = json.dumps(config.body, separators=(",", ":")).encode("utf-8")

        return TransportRequest(
            method=method,
            url=url,
            headers=headers,
            body=body_bytes,
            timeout=timeout,
        )

    def _build_upload_request(
        self,
        url: str,
        body: bytes,
        content_type: str,
        options: RequestOptions | None,
    ) -> TransportRequest:
        request_options = options or RequestOptions()
        timeout = request_options.timeout if request_options.timeout is not None else self._timeout
        headers = merge_headers({"Content-Type": content_type}, request_options.headers)
        return TransportRequest(method="PUT", url=url, headers=headers, body=body, timeout=timeout)

    def _parse_response(self, response: TransportResponse) -> object:
        payload = parse_json_body(response.body, response.headers.get("content-type", ""))
        if response.status < 200 or response.status >= 300:
            raise build_api_error(
                response.status,
                response.headers,
                payload,
                f"ThankYou API request failed with status {response.status}",
            )
        return payload

    def _raise_upload_error(self, response: TransportResponse) -> None:
        if response.status >= 200 and response.status < 300:
            return
        payload = parse_json_body(response.body, response.headers.get("content-type", ""))
        raise build_api_error(
            response.status,
            response.headers,
            payload,
            f"File upload failed with status {response.status}",
        )

    def _resolve_api_key(self) -> str:
        api_key = self._api_key or os.environ.get("THANKYOU_API_KEY")
        if not api_key:
            raise TypeError("api_key is required. Pass api_key or set THANKYOU_API_KEY.")
        return api_key

    async def request(self, config: RequestConfig) -> object:
        method, idempotency_key, auth_api_key, max_retries = self._request_context(config)

        attempt = 0
        while True:
            try:
                return self._parse_response(
                    await self._transport(
                        self._build_request(config, method, idempotency_key, auth_api_key)
                    )
                )
            except Exception as error:
                if attempt >= max_retries or not _should_retry(error):
                    raise
                attempt += 1
                await asyncio.sleep(_retry_delay(attempt))

    async def put_upload(
        self,
        url: str,
        body: bytes,
        content_type: str,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        response = await self._transport(
            self._build_upload_request(url, body, content_type, options)
        )
        self._raise_upload_error(response)


def _blocking_transport(request: TransportRequest) -> TransportResponse:
    urllib_request = URLRequest(
        request.url,
        data=request.body,
        headers=dict(request.headers),
        method=request.method,
    )
    try:
        with urlopen(urllib_request, timeout=request.timeout) as response:
            return TransportResponse(
                status=response.status,
                headers={key.lower(): value for key, value in response.headers.items()},
                body=response.read(),
            )
    except HTTPError as error:
        return TransportResponse(
            status=error.code,
            headers={key.lower(): value for key, value in error.headers.items()},
            body=error.read(),
        )
    except TimeoutError as error:
        raise ThankYouTimeoutError(
            f"Request timed out after {request.timeout}s",
            timeout=request.timeout,
        ) from error
    except URLError as error:
        if isinstance(error.reason, TimeoutError):
            raise ThankYouTimeoutError(
                f"Request timed out after {request.timeout}s",
                timeout=request.timeout,
            ) from error
        raise


async def default_async_transport(request: TransportRequest) -> TransportResponse:
    return await asyncio.to_thread(_blocking_transport, request)


def _should_retry(error: Exception) -> bool:
    if isinstance(error, ThankYouTimeoutError):
        return True
    if isinstance(error, ThankYouAPIError):
        return error.retryable or error.status == 429 or error.status >= 500
    return isinstance(error, (URLError, OSError, TimeoutError))


def _retry_delay(attempt: int) -> float:
    return float(min(2 ** (attempt - 1), 8))
