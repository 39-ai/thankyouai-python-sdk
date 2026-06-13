from __future__ import annotations

from typing import NotRequired, TypedDict


class GenericGenerationOutput(TypedDict, total=False):
    url: str
    mime_type: str
    width: int
    height: int
    duration: int | float
    fps: int | float


class ImageGenerationOutput(GenericGenerationOutput, total=False):
    pass


class VideoGenerationOutput(GenericGenerationOutput, total=False):
    pass


class AudioGenerationOutput(GenericGenerationOutput, total=False):
    pass


class TextGenerationOutput(TypedDict, total=False):
    text: str
    content: str
    url: NotRequired[str]
    mime_type: NotRequired[str]

