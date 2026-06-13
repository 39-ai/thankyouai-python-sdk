from __future__ import annotations

from collections.abc import Mapping
from typing import Any


class ThankYouAPIError(Exception):
    """Base API error with parsed code/type/details plus raw response payload."""

    def __init__(
        self,
        message: str,
        *,
        status: int,
        code: str = "api_error",
        type: str = "api_error",
        retryable: bool = False,
        details: object | None = None,
        headers: Mapping[str, str] | None = None,
        raw: object | None = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.type = type
        self.retryable = retryable
        self.details = details
        self.headers = dict(headers or {})
        self.raw = raw


class ThankYouAuthenticationError(ThankYouAPIError):
    pass


class ThankYouRateLimitError(ThankYouAPIError):
    pass


class ThankYouValidationError(ThankYouAPIError):
    pass


class ThankYouTimeoutError(TimeoutError):
    def __init__(self, message: str, *, timeout: float) -> None:
        super().__init__(message)
        self.timeout = timeout


class ThankYouWebhookVerificationError(ValueError):
    pass


def build_api_error(
    status: int,
    headers: Mapping[str, str],
    payload: object,
    fallback_message: str,
) -> ThankYouAPIError:
    envelope = payload if isinstance(payload, Mapping) else {}
    raw_error = envelope.get("error") if isinstance(envelope, Mapping) else None
    error = raw_error if isinstance(raw_error, Mapping) else {}
    message = (
        str(error.get("message"))
        if isinstance(error.get("message"), str)
        else fallback_message
    )
    code = error.get("code") if isinstance(error.get("code"), str) else f"http_{status}"
    type_ = error.get("type") if isinstance(error.get("type"), str) else _infer_type(status)
    retryable = (
        error.get("retryable")
        if isinstance(error.get("retryable"), bool)
        else status == 429 or status >= 500
    )
    details: Any = error.get("details") if "details" in error else None
    kwargs = {
        "status": status,
        "code": code,
        "type": type_,
        "retryable": retryable,
        "details": details,
        "headers": headers,
        "raw": payload,
    }
    if status in {401, 403} or type_ == "auth_error":
        return ThankYouAuthenticationError(message, **kwargs)
    if status == 429 or type_ == "rate_limit_error":
        return ThankYouRateLimitError(message, **kwargs)
    if status in {400, 409, 413, 422} or type_ == "validation_error":
        return ThankYouValidationError(message, **kwargs)
    return ThankYouAPIError(message, **kwargs)


def _infer_type(status: int) -> str:
    if status in {401, 403}:
        return "auth_error"
    if status == 429:
        return "rate_limit_error"
    if status in {400, 409, 413, 422}:
        return "validation_error"
    return "api_error"
