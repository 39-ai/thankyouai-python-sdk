from __future__ import annotations

import asyncio
import time
from collections.abc import Mapping
from typing import cast
from urllib.parse import quote

from thankyou._client import APIClient, RequestConfig, RequestOptions
from thankyou._utils import (
    DEFAULT_WAIT_INTERVAL_SECONDS,
    DEFAULT_WAIT_TIMEOUT_SECONDS,
    check_deadline,
    create_idempotency_key,
)
from thankyou.resources.generations.inputs import (
    GenerationInput,
    JsonObject,
    JsonValue,
    WebhookConfig,
)
from thankyou.resources.generations.outputs import GenerationOutput
from thankyou.resources.generations.responses import (
    parse_generation_list_response,
    parse_generation_response,
    parse_generation_status_response,
    parse_quote_response,
)
from thankyou.types import (
    GenerationListResponse,
    GenerationResponse,
    GenerationStatus,
    GenerationStatusResponse,
    QuoteResponse,
)

DEFAULT_TERMINAL_STATUSES: set[GenerationStatus] = {
    "succeeded",
    "completed",
    "failed",
    "cancelled",
    "partial_success",
}


class GenerationsResource:
    """Create, inspect, and manage generation jobs."""

    def __init__(self, client: APIClient) -> None:
        self._client = client

    async def create(
        self,
        *,
        model: str | None = None,
        input: GenerationInput | Mapping[str, JsonValue] | None = None,
        webhook: WebhookConfig | Mapping[str, JsonValue] | None = None,
        quote_id: str | None = None,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenerationOutput, JsonObject]:
        """Create a generation, or execute a previously approved quote."""
        response = await self._client.request(
            _create_generation_config(
                model=model,
                input=input,
                webhook=webhook,
                quote_id=quote_id,
                idempotency_key=idempotency_key,
                request_options=request_options,
            )
        )
        return parse_generation_response(response)

    async def run(
        self,
        *,
        model: str | None = None,
        input: GenerationInput | Mapping[str, JsonValue] | None = None,
        webhook: WebhookConfig | Mapping[str, JsonValue] | None = None,
        quote_id: str | None = None,
        idempotency_key: str | None = None,
        interval: float = DEFAULT_WAIT_INTERVAL_SECONDS,
        timeout: float = DEFAULT_WAIT_TIMEOUT_SECONDS,
        terminal_statuses: set[GenerationStatus] | None = None,
        create_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenerationOutput, JsonObject]:
        """Create a generation and wait for the final result."""
        created = await self.create(
            model=model,
            input=input,
            webhook=webhook,
            quote_id=quote_id,
            idempotency_key=idempotency_key,
            request_options=create_options,
        )
        return await self.wait(
            created.id,
            interval=interval,
            timeout=timeout,
            terminal_statuses=terminal_statuses,
        )

    async def retrieve(
        self,
        generation_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenerationOutput, JsonObject]:
        """Retrieve the latest generation record by ID."""
        response = await self._client.request(
            _retrieve_generation_config(generation_id, request_options)
        )
        return parse_generation_response(response)

    async def status(
        self,
        generation_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> GenerationStatusResponse:
        """Retrieve lightweight status and progress for a generation."""
        response = await self._client.request(
            _status_generation_config(generation_id, request_options)
        )
        return parse_generation_status_response(response)

    async def wait(
        self,
        generation_id: str,
        *,
        interval: float = DEFAULT_WAIT_INTERVAL_SECONDS,
        timeout: float = DEFAULT_WAIT_TIMEOUT_SECONDS,
        terminal_statuses: set[GenerationStatus] | None = None,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenerationOutput, JsonObject]:
        """Poll until the generation reaches a terminal status, then return its full record."""
        statuses = terminal_statuses or DEFAULT_TERMINAL_STATUSES
        started_at = time.monotonic()
        while True:
            check_deadline(
                started_at,
                timeout,
                f"Generation {generation_id} did not finish within {timeout}s",
            )
            current = await self.status(generation_id, request_options=request_options)
            if current.status in statuses:
                return await self.retrieve(generation_id, request_options=request_options)
            await asyncio.sleep(interval)

    async def quote(
        self,
        *,
        model: str,
        input: GenerationInput | Mapping[str, JsonValue],
        request_options: RequestOptions | None = None,
    ) -> QuoteResponse[str, JsonObject]:
        """Estimate cost and blocking reasons before creating a generation."""
        response = await self._client.request(
            _quote_generation_config(model, input, request_options)
        )
        return parse_quote_response(response)

    async def list(
        self,
        *,
        page: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        model: str | None = None,
        model_prefix: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> GenerationListResponse[str, GenerationOutput, JsonObject]:
        """List generations visible to the current API key, optionally filtered."""
        response = await self._client.request(
            _list_generations_config(
                page=page,
                page_size=page_size,
                status=status,
                model=model,
                model_prefix=model_prefix,
                request_options=request_options,
            )
        )
        return parse_generation_list_response(response)

    async def cancel(
        self,
        generation_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenerationOutput, JsonObject]:
        """Request cancellation for a generation and return the updated record."""
        response = await self._client.request(
            _cancel_generation_config(generation_id, request_options)
        )
        return parse_generation_response(response)

    async def retry(
        self,
        generation_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenerationOutput, JsonObject]:
        """Retry a failed or retryable generation and return the new record."""
        response = await self._client.request(
            _retry_generation_config(generation_id, request_options)
        )
        return parse_generation_response(response)


def _create_generation_config(
    *,
    model: str | None,
    input: GenerationInput | Mapping[str, JsonValue] | None,
    webhook: WebhookConfig | Mapping[str, JsonValue] | None,
    quote_id: str | None,
    idempotency_key: str | None,
    request_options: RequestOptions | None,
) -> RequestConfig:
    resolved_idempotency_key = idempotency_key
    if resolved_idempotency_key is None and request_options is not None:
        resolved_idempotency_key = request_options.idempotency_key
    resolved_idempotency_key = resolved_idempotency_key or create_idempotency_key()

    if quote_id is not None:
        body: dict[str, object] = {
            "quote_id": quote_id,
            "idempotency_key": resolved_idempotency_key,
        }
    else:
        if model is None:
            raise TypeError("model is required when quote_id is not provided.")
        body = {
            "model": model,
            "input": _copy_json_object(input),
            "idempotency_key": resolved_idempotency_key,
        }
        if webhook is not None:
            body["webhook"] = dict(webhook)

    return RequestConfig(
        method="POST",
        path="/generate",
        body=body,
        idempotent=True,
        options=_with_idempotency_key(
            _without_idempotency_key(request_options),
            resolved_idempotency_key,
        ),
    )


def _retrieve_generation_config(
    generation_id: str,
    request_options: RequestOptions | None,
) -> RequestConfig:
    return RequestConfig(
        method="GET",
        path=f"/generations/{quote(generation_id, safe='')}",
        options=request_options,
    )


def _status_generation_config(
    generation_id: str,
    request_options: RequestOptions | None,
) -> RequestConfig:
    return RequestConfig(
        method="GET",
        path=f"/generations/{quote(generation_id, safe='')}/status",
        options=request_options,
    )


def _quote_generation_config(
    model: str,
    input: GenerationInput | Mapping[str, JsonValue],
    request_options: RequestOptions | None,
) -> RequestConfig:
    return RequestConfig(
        method="POST",
        path="/generate/quote",
        body={"model": model, "input": _copy_json_object(input)},
        options=request_options,
    )


def _list_generations_config(
    *,
    page: int | None,
    page_size: int | None,
    status: str | None,
    model: str | None,
    model_prefix: str | None,
    request_options: RequestOptions | None,
) -> RequestConfig:
    return RequestConfig(
        method="GET",
        path="/generations",
        query={
            "page": page,
            "page_size": page_size,
            "status": status,
            "model": model,
            "model_prefix": model_prefix,
        },
        options=request_options,
    )


def _cancel_generation_config(
    generation_id: str,
    request_options: RequestOptions | None,
) -> RequestConfig:
    return RequestConfig(
        method="POST",
        path=f"/generations/{quote(generation_id, safe='')}/cancel",
        options=request_options,
    )


def _retry_generation_config(
    generation_id: str,
    request_options: RequestOptions | None,
) -> RequestConfig:
    return RequestConfig(
        method="POST",
        path=f"/generations/{quote(generation_id, safe='')}/retry",
        idempotent=True,
        options=request_options,
    )


def _without_idempotency_key(options: RequestOptions | None) -> RequestOptions | None:
    if options is None:
        return None
    return RequestOptions(
        timeout=options.timeout,
        headers=options.headers,
        max_retries=options.max_retries,
    )


def _with_idempotency_key(options: RequestOptions | None, idempotency_key: str) -> RequestOptions:
    return RequestOptions(
        timeout=options.timeout if options else None,
        headers=options.headers if options else None,
        idempotency_key=idempotency_key,
        max_retries=options.max_retries if options else None,
    )


def _copy_json_object(value: GenerationInput | Mapping[str, JsonValue] | None) -> JsonObject:
    return cast(JsonObject, dict(value or {}))


__all__ = ["GenerationsResource"]
