from __future__ import annotations

from collections.abc import Callable
from typing import cast

from thankyou._client import RequestOptions
from thankyou._utils import DEFAULT_WAIT_INTERVAL_SECONDS, DEFAULT_WAIT_TIMEOUT_SECONDS
from thankyou.errors import (
    ThankYouAPIError,
    ThankYouAuthenticationError,
    ThankYouRateLimitError,
    ThankYouTimeoutError,
    ThankYouValidationError,
    ThankYouWebhookVerificationError,
)
from thankyou.resources.files import FilesResource
from thankyou.resources.generations import GenerationsResource
from thankyou.resources.generations.generated import BUILT_IN_MODEL_IDS, BUILT_IN_TASK_IDS
from thankyou.resources.generations.inputs import (
    AspectRatio,
    ImageToImageInput,
    ImageToVideoInput,
    JsonObject,
    JsonPrimitive,
    JsonValue,
    ReferenceAsset,
    TextToImageInput,
    TextToSpeechInput,
    TextToVideoInput,
)
from thankyou.resources.generations.outputs import (
    AudioGenerationOutput,
    GenericGenerationOutput,
    ImageGenerationOutput,
    TextGenerationOutput,
    VideoGenerationOutput,
)
from thankyou.resources.models import ModelsResource
from thankyou.resources.webhooks import WebhooksResource, compute_signature
from thankyou.types import (
    GenerationErrorBody,
    GenerationErrorDetails,
    GenerationFieldError,
    GenerationListResponse,
    GenerationResponse,
    GenerationStatus,
    GenerationStatusResponse,
    ModelDetail,
    ModelListResponse,
    ModelPricing,
    ModelPricingOption,
    ModelSummary,
    QuoteResponse,
    ThankYouWebhookEvent,
    UploadSessionResponse,
    UsageResponse,
)

from ._client import APIClient as _APIClient
from ._client import Transport


class ThankYou:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = "https://api.thankyouai.com/open/v1",
        workspace_id: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 2,
        transport: Transport | None = None,
        default_headers: dict[str, str] | None = None,
    ) -> None:
        client = _APIClient(
            api_key=api_key,
            base_url=base_url,
            workspace_id=workspace_id,
            timeout=timeout,
            max_retries=max_retries,
            transport=transport,
            default_headers=default_headers,
        )
        self.generations = GenerationsResource(client)
        self.models = ModelsResource(client)
        self.files = FilesResource(client)
        self.webhooks = WebhooksResource()

    def run(
        self,
        *,
        model: str | None = None,
        input: object | None = None,
        webhook: JsonObject | None = None,
        quote_id: str | None = None,
        idempotency_key: str | None = None,
        interval: float = DEFAULT_WAIT_INTERVAL_SECONDS,
        timeout: float = DEFAULT_WAIT_TIMEOUT_SECONDS,
        terminal_statuses: set[GenerationStatus] | None = None,
        create_options: RequestOptions | None = None,
    ) -> GenerationResponse[str, GenericGenerationOutput, JsonObject]:
        """Shortcut for `thankyou.generations.run(...)`."""
        run = cast(
            Callable[..., GenerationResponse[str, GenericGenerationOutput, JsonObject]],
            self.generations.run,
        )
        return run(
            model=model,
            input=input,
            webhook=webhook,
            quote_id=quote_id,
            idempotency_key=idempotency_key,
            interval=interval,
            timeout=timeout,
            terminal_statuses=terminal_statuses,
            create_options=create_options,
        )


__all__ = [
    "AspectRatio",
    "AudioGenerationOutput",
    "BUILT_IN_MODEL_IDS",
    "BUILT_IN_TASK_IDS",
    "GenerationErrorBody",
    "GenerationErrorDetails",
    "GenerationFieldError",
    "GenerationListResponse",
    "GenerationResponse",
    "GenerationStatus",
    "GenerationStatusResponse",
    "GenericGenerationOutput",
    "ImageGenerationOutput",
    "ImageToImageInput",
    "ImageToVideoInput",
    "JsonPrimitive",
    "JsonObject",
    "JsonValue",
    "ModelDetail",
    "ModelListResponse",
    "ModelPricing",
    "ModelPricingOption",
    "ModelSummary",
    "QuoteResponse",
    "ReferenceAsset",
    "RequestOptions",
    "TextGenerationOutput",
    "TextToImageInput",
    "TextToSpeechInput",
    "TextToVideoInput",
    "ThankYou",
    "ThankYouAPIError",
    "ThankYouAuthenticationError",
    "ThankYouRateLimitError",
    "ThankYouTimeoutError",
    "ThankYouValidationError",
    "ThankYouWebhookEvent",
    "ThankYouWebhookVerificationError",
    "UploadSessionResponse",
    "UsageResponse",
    "VideoGenerationOutput",
    "compute_signature",
]
