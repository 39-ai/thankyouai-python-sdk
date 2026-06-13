from __future__ import annotations

import hashlib
import hmac
import json
import time

from thankyou._utils import DEFAULT_WEBHOOK_TOLERANCE_SECONDS
from thankyou.errors import ThankYouWebhookVerificationError
from thankyou.resources.generations.responses import parse_generation_response
from thankyou.types import ThankYouWebhookEvent


class WebhooksResource:
    """Verify incoming webhook events before reading their payloads."""

    def verify(
        self,
        *,
        raw_body: str | bytes | bytearray | memoryview,
        signature: str,
        timestamp: str | int,
        secret: str,
        tolerance_seconds: int = DEFAULT_WEBHOOK_TOLERANCE_SECONDS,
    ) -> ThankYouWebhookEvent:
        """Verify a webhook signature and parse the event payload."""
        normalized_timestamp = _normalize_timestamp(timestamp)
        now_seconds = int(time.time())
        if abs(now_seconds - normalized_timestamp) > tolerance_seconds:
            raise ThankYouWebhookVerificationError(
                "Webhook timestamp is outside the allowed tolerance."
            )
        body_text = _normalize_raw_body(raw_body)
        expected = compute_signature(secret, normalized_timestamp, body_text)
        if not hmac.compare_digest(signature.strip(), expected):
            raise ThankYouWebhookVerificationError("Webhook signature is invalid.")
        try:
            payload = json.loads(body_text)
        except json.JSONDecodeError as error:
            raise ThankYouWebhookVerificationError(
                f"Webhook body is not valid JSON: {error}"
            ) from error
        if not isinstance(payload, dict):
            raise ThankYouWebhookVerificationError("Webhook body is not a JSON object.")
        generation = payload.get("generation")
        return ThankYouWebhookEvent(
            event=str(payload.get("event", "")),
            generation=parse_generation_response(generation) if generation is not None else None,
            data={
                key: value
                for key, value in payload.items()
                if key not in {"event", "generation"}
            },
        )


def compute_signature(
    secret: str,
    timestamp: str | int,
    raw_body: str | bytes | bytearray | memoryview,
) -> str:
    """Compute the expected `sha256=<hex>` webhook signature."""
    normalized_timestamp = _normalize_timestamp(timestamp)
    body_text = _normalize_raw_body(raw_body)
    digest = hmac.new(
        secret.encode("utf-8"),
        f"{normalized_timestamp}.{body_text}".encode(),
        hashlib.sha256,
    ).hexdigest()
    return f"sha256={digest}"


def _normalize_timestamp(timestamp: str | int) -> int:
    try:
        return int(timestamp)
    except ValueError as error:
        raise ThankYouWebhookVerificationError("Webhook timestamp is invalid.") from error


def _normalize_raw_body(raw_body: str | bytes | bytearray | memoryview) -> str:
    if isinstance(raw_body, str):
        return raw_body
    return bytes(raw_body).decode("utf-8")
