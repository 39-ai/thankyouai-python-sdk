from __future__ import annotations

import asyncio
from pathlib import Path

from thankyou._client import APIClient, RequestConfig, RequestOptions
from thankyou._utils import as_dict, read_upload_body
from thankyou.types import UploadSessionResponse


class FilesResource:
    """Helpers for preparing files that can be referenced by generation inputs."""

    def __init__(self, client: APIClient) -> None:
        self._client = client

    async def create_upload_session(
        self,
        *,
        content_type: str,
        size_bytes: int,
        filename: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> UploadSessionResponse:
        """Create an upload session and return the upload URL plus public file URL."""
        response = await self._client.request(
            _create_upload_session_config(
                content_type=content_type,
                size_bytes=size_bytes,
                filename=filename,
                request_options=request_options,
            )
        )
        return _parse_upload_session(response)

    async def upload(
        self,
        *,
        file: str | Path | bytes | bytearray | memoryview,
        filename: str | None = None,
        content_type: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> UploadSessionResponse:
        """Upload a local path or bytes object and return metadata for later generation inputs."""
        body, resolved_filename, resolved_content_type = await asyncio.to_thread(
            read_upload_body,
            file,
            filename=filename,
            content_type=content_type,
        )
        session = await self.create_upload_session(
            content_type=resolved_content_type,
            size_bytes=len(body),
            filename=resolved_filename,
            request_options=request_options,
        )
        await self._client.put_upload(
            session.upload_url,
            body,
            resolved_content_type,
            options=_upload_request_options(request_options),
        )
        return session


def _create_upload_session_config(
    *,
    content_type: str,
    size_bytes: int,
    filename: str | None,
    request_options: RequestOptions | None,
) -> RequestConfig:
    return RequestConfig(
        method="POST",
        path="/files",
        body={
            "content_type": content_type,
            "filename": filename,
            "size_bytes": size_bytes,
        },
        options=request_options,
    )


def _upload_request_options(request_options: RequestOptions | None) -> RequestOptions:
    return RequestOptions(timeout=request_options.timeout if request_options else None)


def _parse_upload_session(response: object) -> UploadSessionResponse:
    data = as_dict(response)
    return UploadSessionResponse(
        upload_url=str(data["upload_url"]),
        upload_url_expires_at=str(data["upload_url_expires_at"]),
        file_id=str(data["file_id"]),
        url=str(data["url"]),
        content_type=str(data["content_type"]),
        size_bytes=int(data["size_bytes"]),
        url_expires_at=str(data["url_expires_at"]),
    )
