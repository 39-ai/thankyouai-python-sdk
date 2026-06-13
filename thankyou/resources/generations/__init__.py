from __future__ import annotations

import time
from collections.abc import Mapping
from urllib.parse import quote

from thankyou._client import APIClient, RequestConfig, RequestOptions
from thankyou._utils import (
    DEFAULT_WAIT_INTERVAL_SECONDS,
    DEFAULT_WAIT_TIMEOUT_SECONDS,
    check_deadline,
    create_idempotency_key,
    sleep,
)
from thankyou.resources.generations.inputs import GenericGenerationInput
from thankyou.resources.generations.outputs import GenericGenerationOutput
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
    def __init__(self, client: APIClient) -> None:
        self._client = client

    def create(
        self,
        *,
        model: str | None = None,
        input: Mapping[str, object] | None = None,
        webhook: Mapping[str, object] | None = None,
        quote_id: str | None = None,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]:
        """Creates a generation, or executes a previously approved quote."""
        resolved_idempotency_key = idempotency_key
        if resolved_idempotency_key is None and request_options is not None:
            resolved_idempotency_key = request_options.idempotency_key
        resolved_idempotency_key = resolved_idempotency_key or create_idempotency_key()
        options = _without_idempotency_key(request_options)
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
                "input": dict(input or {}),
                "idempotency_key": resolved_idempotency_key,
            }
            if webhook is not None:
                body["webhook"] = dict(webhook)
        response = self._client.request(
            RequestConfig(
                method="POST",
                path="/generate",
                body=body,
                idempotent=True,
                options=_with_idempotency_key(options, resolved_idempotency_key),
            )
        )
        return parse_generation_response(response)

    def run(
        self,
        *,
        model: str | None = None,
        input: Mapping[str, object] | None = None,
        webhook: Mapping[str, object] | None = None,
        quote_id: str | None = None,
        idempotency_key: str | None = None,
        interval: float = DEFAULT_WAIT_INTERVAL_SECONDS,
        timeout: float = DEFAULT_WAIT_TIMEOUT_SECONDS,
        terminal_statuses: set[GenerationStatus] | None = None,
        create_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]:
        """Creates a generation and waits until it reaches a terminal status."""
        created = self.create(
            model=model,
            input=input,
            webhook=webhook,
            quote_id=quote_id,
            idempotency_key=idempotency_key,
            request_options=create_options,
        )
        return self.wait(
            created.id,
            interval=interval,
            timeout=timeout,
            terminal_statuses=terminal_statuses,
        )

    def retrieve(
        self,
        generation_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]:
        """Retrieves the latest generation record by ID."""
        response = self._client.request(
            RequestConfig(
                method="GET",
                path=f"/generations/{quote(generation_id, safe='')}",
                options=request_options,
            )
        )
        return parse_generation_response(response)

    def status(
        self,
        generation_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> GenerationStatusResponse:
        """Retrieves only the current status for a generation."""
        response = self._client.request(
            RequestConfig(
                method="GET",
                path=f"/generations/{quote(generation_id, safe='')}/status",
                options=request_options,
            )
        )
        return parse_generation_status_response(response)

    def wait(
        self,
        generation_id: str,
        *,
        interval: float = DEFAULT_WAIT_INTERVAL_SECONDS,
        timeout: float = DEFAULT_WAIT_TIMEOUT_SECONDS,
        terminal_statuses: set[GenerationStatus] | None = None,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]:
        """Polls a generation until it reaches a terminal status, then returns the full record."""
        statuses = terminal_statuses or DEFAULT_TERMINAL_STATUSES
        started_at = time.monotonic()
        while True:
            check_deadline(
                started_at,
                timeout,
                f"Generation {generation_id} did not finish within {timeout}s",
            )
            current = self.status(generation_id, request_options=request_options)
            if current.status in statuses:
                return self.retrieve(generation_id, request_options=request_options)
            sleep(interval)

    def quote(
        self,
        *,
        model: str,
        input: Mapping[str, object],
        request_options: RequestOptions | None = None,
    ) -> QuoteResponse[str, GenericGenerationInput]:
        """Estimates cost and eligibility before creating a generation."""
        response = self._client.request(
            RequestConfig(
                method="POST",
                path="/generate/quote",
                body={"model": model, "input": dict(input)},
                options=request_options,
            )
        )
        return parse_quote_response(response)

    def list(
        self,
        *,
        page: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        model: str | None = None,
        model_prefix: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> GenerationListResponse[str, GenericGenerationOutput, GenericGenerationInput]:
        """Lists generations visible to the current API key."""
        response = self._client.request(
            RequestConfig(
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
        )
        return parse_generation_list_response(response)

    def cancel(
        self,
        generation_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]:
        """Requests cancellation for a generation."""
        response = self._client.request(
            RequestConfig(
                method="POST",
                path=f"/generations/{quote(generation_id, safe='')}/cancel",
                options=request_options,
            )
        )
        return parse_generation_response(response)

    def retry(
        self,
        generation_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]:
        """Retries a failed or retryable generation."""
        response = self._client.request(
            RequestConfig(
                method="POST",
                path=f"/generations/{quote(generation_id, safe='')}/retry",
                idempotent=True,
                options=request_options,
            )
        )
        return parse_generation_response(response)


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


__all__ = ["GenerationsResource"]
