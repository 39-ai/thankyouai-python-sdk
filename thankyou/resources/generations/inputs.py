from __future__ import annotations

from typing import NotRequired, Required, TypeAlias, TypedDict

JsonPrimitive: TypeAlias = str | int | float | bool | None
JsonValue: TypeAlias = JsonPrimitive | dict[str, "JsonValue"] | list["JsonValue"]
JsonObject: TypeAlias = dict[str, JsonValue]


class ReferenceAsset(TypedDict, total=False):
    role: Required[str]
    asset_id: str
    url: str


class GenerationInput(TypedDict, total=False):
    """Common generation input fields.

    The API accepts model-specific fields beyond these keys. For those fields,
    pass a normal ``dict[str, JsonValue]`` or a ``JsonObject`` after checking
    ``GET /open/v1/models/detail?model_id=...``.
    """

    prompt: str
    text: str
    negative_prompt: str
    reference_assets: list[ReferenceAsset]
    aspect_ratio: str
    duration: str
    num_images: int


class WebhookConfig(TypedDict, total=False):
    url: Required[str]
    events: NotRequired[list[str]]


class CreateGenerationRequest(TypedDict, total=False):
    model: str
    input: GenerationInput | JsonObject
    webhook: WebhookConfig | JsonObject
    idempotency_key: str
    quote_id: str


class QuoteGenerationRequest(TypedDict):
    model: str
    input: GenerationInput | JsonObject
