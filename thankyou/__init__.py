from __future__ import annotations

from thankyou._client import RequestOptions
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
    GenericGenerationInput,
    ImageToImageInput,
    ImageToVideoInput,
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
        **kwargs: object,
    ) -> GenerationResponse[str, GenericGenerationOutput, GenericGenerationInput]:
        """Shortcut for `thankyou.generations.run(...)`."""
        return self.generations.run(**kwargs)


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
    "GenericGenerationInput",
    "GenericGenerationOutput",
    "ImageGenerationOutput",
    "ImageToImageInput",
    "ImageToVideoInput",
    "JsonPrimitive",
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
