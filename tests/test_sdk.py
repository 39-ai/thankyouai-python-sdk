from __future__ import annotations

import asyncio
import json
import time
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import pytest

from thankyou import (
    AsyncThankYou,
    GenerationInput,
    RequestOptions,
    ThankYou,
    ThankYouAuthenticationError,
    ThankYouRateLimitError,
    ThankYouValidationError,
    ThankYouWebhookVerificationError,
    compute_signature,
)
from thankyou._client import TransportRequest, TransportResponse


@dataclass
class RecordedCall:
    request: TransportRequest


class MockTransport:
    def __init__(
        self,
        responses: list[
            TransportResponse | Exception | Callable[[TransportRequest], TransportResponse]
        ],
    ) -> None:
        self.responses = responses
        self.calls: list[RecordedCall] = []

    def __call__(self, request: TransportRequest) -> TransportResponse:
        self.calls.append(RecordedCall(request))
        if not self.responses:
            raise AssertionError("Unexpected request")
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        if callable(response):
            return response(request)
        return response


class AsyncMockTransport:
    def __init__(
        self,
        responses: list[
            TransportResponse | Exception | Callable[[TransportRequest], TransportResponse]
        ],
    ) -> None:
        self._sync = MockTransport(responses)

    @property
    def calls(self) -> list[RecordedCall]:
        return self._sync.calls

    async def __call__(self, request: TransportRequest) -> TransportResponse:
        return self._sync(request)


def json_response(
    body: object,
    status: int = 200,
    headers: dict[str, str] | None = None,
) -> TransportResponse:
    return TransportResponse(
        status=status,
        headers={"content-type": "application/json", **(headers or {})},
        body=json.dumps(body).encode("utf-8"),
    )


def text_response(body: str, status: int = 200) -> TransportResponse:
    return TransportResponse(status=status, headers={}, body=body.encode("utf-8"))


GENERATION = {
    "id": "gen_123",
    "status": "queued",
    "model": "flux/v2/pro/text-to-image",
    "output": [],
    "usage": {"credits_consumed": 0, "currency": "points"},
    "progress": 0,
    "params_raw": {},
    "resolved_params": {},
    "created_at": "2026-06-13T00:00:00Z",
}


def test_common_generation_input_keeps_documented_fields_and_allows_custom_dicts() -> None:
    common_input: GenerationInput = {
        "prompt": "A mountain landscape",
        "reference_assets": [{"role": "primary", "url": "https://example.test/image.jpg"}],
        "aspect_ratio": "16:9",
        "duration": "5",
        "num_images": 1,
    }
    model_specific_input: dict[str, object] = {
        **common_input,
        "resolution": "1080P",
        "camera_fixed": False,
    }

    assert model_specific_input["resolution"] == "1080P"


def test_sends_auth_headers_workspace_id_default_headers_base_url_and_create_body() -> None:
    transport = MockTransport([json_response(GENERATION, 202)])
    thankyou = ThankYou(
        api_key="tk_test",
        base_url="https://example.test/open/v1/",
        workspace_id="ws_1",
        default_headers={"x-custom": "yes"},
        transport=transport,
    )

    created = thankyou.generations.create(
        model="flux/v2/pro/text-to-image",
        input={"prompt": "A mountain landscape"},
        idempotency_key="idem_1",
    )

    assert created.created_at == datetime.fromisoformat("2026-06-13T00:00:00+00:00")
    call = transport.calls[0].request
    assert call.url == "https://example.test/open/v1/generate"
    assert call.headers["Authorization"] == "Bearer tk_test"
    assert call.headers["x-workspace-id"] == "ws_1"
    assert call.headers["x-custom"] == "yes"
    assert call.headers["Idempotency-Key"] == "idem_1"
    assert json.loads(call.body or b"{}") == {
        "model": "flux/v2/pro/text-to-image",
        "input": {"prompt": "A mountain landscape"},
        "idempotency_key": "idem_1",
    }


def test_retrieves_generation_lightweight_status_and_quote() -> None:
    transport = MockTransport([
        json_response(GENERATION),
        json_response({"id": "gen_123", "status": "running", "progress": 0.5, "finished_at": None}),
        json_response({
            "quote_id": "quote_1",
            "model": "wan/v2.6/text-to-video",
            "estimated_cost": 0.75,
            "currency": "points",
            "blocking_reasons": [],
            "resolved_params": {},
            "expires_at": "2026-06-13T00:10:00Z",
        }),
    ])
    thankyou = ThankYou(api_key="tk_test", transport=transport)

    retrieved = thankyou.generations.retrieve("gen_123")
    status = thankyou.generations.status("gen_123")
    quote = thankyou.generations.quote(model="wan/v2.6/text-to-video", input={"prompt": "test"})

    assert retrieved.created_at == datetime.fromisoformat("2026-06-13T00:00:00+00:00")
    assert status.finished_at is None
    assert quote.expires_at == datetime.fromisoformat("2026-06-13T00:10:00+00:00")
    assert [(call.request.method, call.request.url) for call in transport.calls] == [
        ("GET", "https://api.thankyouai.com/open/v1/generations/gen_123"),
        ("GET", "https://api.thankyouai.com/open/v1/generations/gen_123/status"),
        ("POST", "https://api.thankyouai.com/open/v1/generate/quote"),
    ]


def test_auto_generates_idempotency_keys_for_create() -> None:
    transport = MockTransport([json_response(GENERATION, 202)])
    thankyou = ThankYou(api_key="tk_test", transport=transport)

    thankyou.generations.create(
        model="flux/v2/pro/text-to-image",
        input={"prompt": "A mountain landscape"},
    )

    body = json.loads(transport.calls[0].request.body or b"{}")
    assert body["idempotency_key"].startswith("ty_")
    assert transport.calls[0].request.headers["Idempotency-Key"] == body["idempotency_key"]


def test_reads_api_key_from_environment_when_omitted(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("THANKYOU_API_KEY", "tk_env")
    transport = MockTransport([json_response(GENERATION)])
    thankyou = ThankYou(transport=transport)

    thankyou.generations.retrieve("gen_123")

    assert transport.calls[0].request.headers["Authorization"] == "Bearer tk_env"


def test_requires_api_key_before_authenticated_requests(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("THANKYOU_API_KEY", raising=False)
    transport = MockTransport([json_response(GENERATION)])
    thankyou = ThankYou(transport=transport)

    with pytest.raises(TypeError, match="api_key is required"):
        thankyou.generations.retrieve("gen_123")
    assert transport.calls == []


def test_wait_polls_status_until_terminal_and_retrieves_full_generation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(time, "sleep", lambda _: None)
    transport = MockTransport([
        json_response({"id": "gen_123", "status": "queued", "progress": 0, "finished_at": None}),
        json_response({
            "id": "gen_123",
            "status": "succeeded",
            "progress": 1,
            "finished_at": "2026-06-13T00:01:00Z",
        }),
        json_response({
            **GENERATION,
            "status": "succeeded",
            "started_at": "2026-06-13T00:00:30Z",
            "finished_at": "2026-06-13T00:01:00Z",
            "output": [{"url": "https://static.example/1.jpg"}],
        }),
    ])
    thankyou = ThankYou(api_key="tk_test", transport=transport)

    result = thankyou.generations.wait("gen_123", interval=0.01, timeout=1)

    assert result.output[0].get("url") == "https://static.example/1.jpg"
    assert result.started_at == datetime.fromisoformat("2026-06-13T00:00:30+00:00")
    assert result.finished_at == datetime.fromisoformat("2026-06-13T00:01:00+00:00")
    assert len(transport.calls) == 3


def test_top_level_run_creates_and_waits_for_final_result(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(time, "sleep", lambda _: None)
    transport = MockTransport([
        json_response(GENERATION, 202),
        json_response({"id": "gen_123", "status": "queued", "progress": 0, "finished_at": None}),
        json_response({
            "id": "gen_123",
            "status": "succeeded",
            "progress": 1,
            "finished_at": "2026-06-13T00:01:00Z",
        }),
        json_response({
            **GENERATION,
            "status": "succeeded",
            "finished_at": "2026-06-13T00:01:00Z",
            "output": [{"url": "https://static.example/final.jpg", "mime_type": "image/jpeg"}],
        }),
    ])
    thankyou = ThankYou(api_key="tk_test", transport=transport)

    result = thankyou.run(
        model="flux/v2/pro/text-to-image",
        input={"prompt": "A mountain landscape"},
        interval=0.01,
        timeout=1,
        create_options=RequestOptions(headers={"x-create": "yes"}),
    )

    assert result.output[0].get("url") == "https://static.example/final.jpg"
    assert result.finished_at == datetime.fromisoformat("2026-06-13T00:01:00+00:00")
    assert [(call.request.method, call.request.url) for call in transport.calls] == [
        ("POST", "https://api.thankyouai.com/open/v1/generate"),
        ("GET", "https://api.thankyouai.com/open/v1/generations/gen_123/status"),
        ("GET", "https://api.thankyouai.com/open/v1/generations/gen_123/status"),
        ("GET", "https://api.thankyouai.com/open/v1/generations/gen_123"),
    ]
    assert transport.calls[0].request.headers["x-create"] == "yes"


def test_async_top_level_run_creates_and_waits_for_final_result(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def no_sleep(_: float) -> None:
        return None

    monkeypatch.setattr(asyncio, "sleep", no_sleep)
    transport = AsyncMockTransport([
        json_response(GENERATION, 202),
        json_response({"id": "gen_123", "status": "queued", "progress": 0, "finished_at": None}),
        json_response({
            "id": "gen_123",
            "status": "succeeded",
            "progress": 1,
            "finished_at": "2026-06-13T00:01:00Z",
        }),
        json_response({
            **GENERATION,
            "status": "succeeded",
            "finished_at": "2026-06-13T00:01:00Z",
            "output": [{"url": "https://static.example/final.jpg", "mime_type": "image/jpeg"}],
        }),
    ])
    thankyou = AsyncThankYou(api_key="tk_test", transport=transport)

    async def run() -> None:
        result = await thankyou.run(
            model="flux/v2/pro/text-to-image",
            input={"prompt": "A mountain landscape"},
            interval=0.01,
            timeout=1,
            create_options=RequestOptions(headers={"x-create": "yes"}),
        )

        assert result.output[0].get("url") == "https://static.example/final.jpg"
        assert result.finished_at == datetime.fromisoformat("2026-06-13T00:01:00+00:00")

    asyncio.run(run())

    assert [(call.request.method, call.request.url) for call in transport.calls] == [
        ("POST", "https://api.thankyouai.com/open/v1/generate"),
        ("GET", "https://api.thankyouai.com/open/v1/generations/gen_123/status"),
        ("GET", "https://api.thankyouai.com/open/v1/generations/gen_123/status"),
        ("GET", "https://api.thankyouai.com/open/v1/generations/gen_123"),
    ]
    assert transport.calls[0].request.headers["x-create"] == "yes"


def test_top_level_run_rejects_unknown_keyword_arguments() -> None:
    thankyou = ThankYou(api_key="tk_test", transport=MockTransport([]))

    with pytest.raises(TypeError, match="unexpected keyword argument"):
        thankyou.run(  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
            model="flux/v2/pro/text-to-image",
            input={},
            unexpected=True,
        )


def test_parses_dates_in_listed_generations() -> None:
    transport = MockTransport([
        json_response({
            "generations": [
                {
                    **GENERATION,
                    "started_at": "2026-06-13T00:00:30Z",
                    "finished_at": "2026-06-13T00:01:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "page_size": 20,
        })
    ])
    thankyou = ThankYou(api_key="tk_test", transport=transport)

    listed = thankyou.generations.list()

    assert listed.generations[0].created_at == datetime.fromisoformat("2026-06-13T00:00:00+00:00")
    assert listed.generations[0].started_at == datetime.fromisoformat("2026-06-13T00:00:30+00:00")
    assert listed.generations[0].finished_at == datetime.fromisoformat("2026-06-13T00:01:00+00:00")


def test_lists_models_and_gets_detail_without_auth() -> None:
    transport = MockTransport([
        json_response({"models": []}),
        json_response({
            "id": "wan/v2.6/text-to-video",
            "display_name": "WAN 2.6",
            "description": "",
            "operation": "text-to-video",
            "category": "video-generation",
            "supported_modes": [],
            "providers": [],
            "vendor": "wan",
            "audio_support": "off",
            "badges": [],
            "features": [],
            "preview_image": "",
            "default_mode": "",
            "default_params": {},
            "input_schema": {},
            "primary_fields": [],
            "advanced_fields": [],
            "resolution_map": {},
        }),
    ])
    thankyou = ThankYou(api_key="tk_test", transport=transport)

    thankyou.models.list()
    detail = thankyou.models.detail("wan/v2.6/text-to-video")

    assert transport.calls[0].request.url == "https://api.thankyouai.com/open/v1/models"
    assert "Authorization" not in transport.calls[0].request.headers
    assert transport.calls[1].request.url == "https://api.thankyouai.com/open/v1/models/detail?model_id=wan%2Fv2.6%2Ftext-to-video"
    assert "Authorization" not in transport.calls[1].request.headers
    assert detail.id == "wan/v2.6/text-to-video"


def test_async_lists_models_and_gets_detail_without_auth() -> None:
    transport = AsyncMockTransport([
        json_response({"models": []}),
        json_response({
            "id": "wan/v2.6/text-to-video",
            "display_name": "WAN 2.6",
            "description": "",
            "operation": "text-to-video",
            "category": "video-generation",
            "supported_modes": [],
            "providers": [],
            "vendor": "wan",
            "audio_support": "off",
            "badges": [],
            "features": [],
            "preview_image": "",
            "default_mode": "",
            "default_params": {},
            "input_schema": {},
            "primary_fields": [],
            "advanced_fields": [],
            "resolution_map": {},
        }),
    ])
    thankyou = AsyncThankYou(api_key="tk_test", transport=transport)

    async def run() -> None:
        await thankyou.models.list()
        detail = await thankyou.models.detail("wan/v2.6/text-to-video")
        assert detail.id == "wan/v2.6/text-to-video"

    asyncio.run(run())

    assert transport.calls[0].request.url == "https://api.thankyouai.com/open/v1/models"
    assert "Authorization" not in transport.calls[0].request.headers
    assert transport.calls[1].request.url == "https://api.thankyouai.com/open/v1/models/detail?model_id=wan%2Fv2.6%2Ftext-to-video"
    assert "Authorization" not in transport.calls[1].request.headers


def test_creates_upload_session_and_puts_bytes_without_authorization() -> None:
    transport = MockTransport([
        json_response({
            "upload_url": "https://uploads.example/put",
            "upload_url_expires_at": "2026-06-13T00:15:00Z",
            "file_id": "file_1",
            "url": "https://static.example/file.jpg",
            "content_type": "image/jpeg",
            "size_bytes": 4,
            "url_expires_at": "2026-06-14T00:00:00Z",
        }, 201),
        text_response("", 200),
    ])
    thankyou = ThankYou(api_key="tk_test", transport=transport)

    uploaded = thankyou.files.upload(file=bytes([1, 2, 3, 4]), filename="photo.jpg")

    assert uploaded.file_id == "file_1"
    assert transport.calls[0].request.url == "https://api.thankyouai.com/open/v1/files"
    assert json.loads(transport.calls[0].request.body or b"{}") == {
        "content_type": "image/jpeg",
        "filename": "photo.jpg",
        "size_bytes": 4,
    }
    assert transport.calls[1].request.url == "https://uploads.example/put"
    assert transport.calls[1].request.headers["Content-Type"] == "image/jpeg"
    assert "Authorization" not in transport.calls[1].request.headers


def test_async_creates_upload_session_and_puts_bytes_without_authorization() -> None:
    transport = AsyncMockTransport([
        json_response({
            "upload_url": "https://uploads.example/put",
            "upload_url_expires_at": "2026-06-13T00:15:00Z",
            "file_id": "file_1",
            "url": "https://static.example/file.jpg",
            "content_type": "image/jpeg",
            "size_bytes": 4,
            "url_expires_at": "2026-06-14T00:00:00Z",
        }, 201),
        text_response("", 200),
    ])
    thankyou = AsyncThankYou(api_key="tk_test", transport=transport)

    async def run() -> None:
        uploaded = await thankyou.files.upload(file=bytes([1, 2, 3, 4]), filename="photo.jpg")
        assert uploaded.file_id == "file_1"

    asyncio.run(run())

    assert transport.calls[0].request.url == "https://api.thankyouai.com/open/v1/files"
    assert json.loads(transport.calls[0].request.body or b"{}") == {
        "content_type": "image/jpeg",
        "filename": "photo.jpg",
        "size_bytes": 4,
    }
    assert transport.calls[1].request.url == "https://uploads.example/put"
    assert transport.calls[1].request.headers["Content-Type"] == "image/jpeg"
    assert "Authorization" not in transport.calls[1].request.headers


def test_upload_accepts_file_paths(tmp_path: Path) -> None:
    path = tmp_path / "photo.jpg"
    path.write_bytes(b"1234")
    transport = MockTransport([
        json_response({
            "upload_url": "https://uploads.example/put",
            "upload_url_expires_at": "2026-06-13T00:15:00Z",
            "file_id": "file_1",
            "url": "https://static.example/file.jpg",
            "content_type": "image/jpeg",
            "size_bytes": 4,
            "url_expires_at": "2026-06-14T00:00:00Z",
        }, 201),
        text_response("", 200),
    ])
    thankyou = ThankYou(api_key="tk_test", transport=transport)

    thankyou.files.upload(file=path)

    assert json.loads(transport.calls[0].request.body or b"{}")["filename"] == "photo.jpg"


def test_maps_error_envelopes_to_typed_errors_and_preserves_details() -> None:
    auth = MockTransport([
        json_response({
            "error": {
                "code": "invalid_api_key",
                "type": "auth_error",
                "message": "Invalid API key",
                "retryable": False,
            }
        }, 401)
    ])
    with pytest.raises(ThankYouAuthenticationError):
        ThankYou(api_key="tk_bad", transport=auth).generations.retrieve("x")

    rate = MockTransport([
        json_response({
            "error": {
                "code": "rate_limited",
                "type": "rate_limit_error",
                "message": "Slow down",
                "retryable": True,
                "details": {"limit": 1},
            }
        }, 429)
    ])
    with pytest.raises(ThankYouRateLimitError) as rate_error:
        ThankYou(api_key="tk_test", transport=rate, max_retries=0).generations.retrieve("x")
    assert rate_error.value.details == {"limit": 1}

    validation = MockTransport([
        json_response({
            "error": {
                "code": "invalid_model",
                "type": "validation_error",
                "message": "Invalid model",
                "retryable": False,
            }
        }, 422)
    ])
    with pytest.raises(ThankYouValidationError):
        ThankYou(api_key="tk_test", transport=validation).generations.retrieve("x")


def test_retries_retryable_responses_and_network_errors() -> None:
    transport = MockTransport([
        json_response({
            "error": {
                "code": "temporary",
                "type": "api_error",
                "message": "temporary",
                "retryable": True,
            }
        }, 500),
        OSError("network failed"),
        json_response(GENERATION),
    ])
    thankyou = ThankYou(api_key="tk_test", transport=transport, max_retries=2)

    result = thankyou.generations.retrieve("gen_123")

    assert result.id == "gen_123"
    assert len(transport.calls) == 3


def test_verifies_webhook_signature_and_parses_generation() -> None:
    timestamp = str(int(time.time()))
    body = json.dumps({
        "event": "generation.completed",
        "generation": {
            **GENERATION,
            "status": "succeeded",
            "finished_at": "2026-06-13T00:01:00Z",
        },
    })
    signature = compute_signature("whsec_test", timestamp, body)
    thankyou = ThankYou(api_key="tk_test", transport=MockTransport([]))

    event = thankyou.webhooks.verify(
        raw_body=body,
        signature=signature,
        timestamp=timestamp,
        secret="whsec_test",
    )

    assert event.event == "generation.completed"
    assert event.generation is not None
    assert event.generation.finished_at == datetime.fromisoformat("2026-06-13T00:01:00+00:00")


def test_rejects_invalid_webhook_signature() -> None:
    thankyou = ThankYou(api_key="tk_test", transport=MockTransport([]))

    with pytest.raises(ThankYouWebhookVerificationError):
        thankyou.webhooks.verify(
            raw_body="{}",
            signature="sha256=bad",
            timestamp=str(int(time.time())),
            secret="whsec_test",
        )
