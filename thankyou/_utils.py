from __future__ import annotations

import json
import mimetypes
import time
import uuid
from collections.abc import Mapping
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

from .errors import ThankYouTimeoutError

DEFAULT_BASE_URL = "https://api.thankyouai.com/open/v1"
DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_MAX_RETRIES = 2
DEFAULT_WAIT_INTERVAL_SECONDS = 2.0
DEFAULT_WAIT_TIMEOUT_SECONDS = 10 * 60.0
DEFAULT_WEBHOOK_TOLERANCE_SECONDS = 300


def normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


def build_query(params: Mapping[str, object | None]) -> str:
    clean = {key: str(value) for key, value in params.items() if value is not None}
    return f"?{urlencode(clean)}" if clean else ""


def merge_headers(*headers: Mapping[str, str] | None) -> dict[str, str]:
    result: dict[str, str] = {}
    for item in headers:
        if not item:
            continue
        for key, value in item.items():
            result[key] = value
    return result


def create_idempotency_key() -> str:
    return f"ty_{uuid.uuid4()}"


def check_deadline(started_at: float, timeout: float, message: str) -> None:
    if time.monotonic() - started_at > timeout:
        raise ThankYouTimeoutError(message, timeout=timeout)


def parse_json_body(body: bytes, content_type: str) -> object:
    if not body:
        return None
    text = body.decode("utf-8")
    if "application/json" in content_type:
        return json.loads(text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def parse_datetime(value: str | datetime) -> datetime:
    if isinstance(value, datetime):
        return value
    text = value[:-1] + "+00:00" if value.endswith("Z") else value
    return datetime.fromisoformat(text)


def parse_optional_datetime(value: str | datetime | None) -> datetime | None:
    if value is None:
        return None
    return parse_datetime(value)


def infer_content_type(filename: str | None) -> str | None:
    if not filename:
        return None
    guessed, _ = mimetypes.guess_type(filename)
    return guessed


def read_upload_body(
    file: str | Path | bytes | bytearray | memoryview,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> tuple[bytes, str | None, str]:
    if isinstance(file, str | Path):
        path = Path(file)
        data = path.read_bytes()
        resolved_filename = filename or path.name
        resolved_content_type = content_type or infer_content_type(resolved_filename)
        if not resolved_content_type:
            raise TypeError(
                "content_type is required when it cannot be inferred from the file extension."
            )
        return data, resolved_filename, resolved_content_type

    data = bytes(file)
    resolved_content_type = content_type or infer_content_type(filename)
    if not resolved_content_type:
        raise TypeError("content_type is required for byte uploads.")
    return data, filename, resolved_content_type


def as_dict(value: object) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    raise TypeError("Expected a JSON object response.")
