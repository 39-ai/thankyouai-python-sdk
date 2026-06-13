from __future__ import annotations

from typing import Literal, NotRequired, TypeAlias, TypedDict

JsonPrimitive: TypeAlias = str | int | float | bool | None
JsonValue: TypeAlias = JsonPrimitive | dict[str, "JsonValue"] | list["JsonValue"]
JsonObject: TypeAlias = dict[str, JsonValue]

AspectRatio: TypeAlias = Literal["1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"]


class ReferenceAsset(TypedDict, total=False):
    url: str
    file_id: str
    mime_type: str


class TextToImageInput(TypedDict, total=False):
    prompt: str
    negative_prompt: str
    aspect_ratio: AspectRatio
    seed: int
    width: int
    height: int


class TextToVideoInput(TypedDict, total=False):
    prompt: str
    negative_prompt: str
    aspect_ratio: AspectRatio
    duration: int | float
    resolution: str
    seed: int
    enhance_prompt: bool


class ImageToVideoInput(TextToVideoInput, total=False):
    reference_assets: list[ReferenceAsset]
    image_url: str
    start_image_url: str
    end_image_url: str


class ImageToImageInput(TypedDict):
    reference_assets: list[ReferenceAsset]
    prompt: NotRequired[str]
    strength: NotRequired[int | float]
    seed: NotRequired[int]


class TextToSpeechInput(TypedDict, total=False):
    text: str
    voice: str
    speed: int | float
    format: Literal["mp3", "wav", "m4a", "ogg"]
