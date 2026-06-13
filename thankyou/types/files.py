from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UploadSessionResponse:
    upload_url: str
    upload_url_expires_at: str
    file_id: str
    url: str
    content_type: str
    size_bytes: int
    url_expires_at: str

