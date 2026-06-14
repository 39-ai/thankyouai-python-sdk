from __future__ import annotations

from typing import TypedDict


class GenerationOutput(TypedDict, total=False):
    """Common generation output item fields.

    The API may return additional model-specific fields. For those fields, read
    the output item as a normal ``dict`` at runtime or cast it to ``JsonObject``.
    """

    url: str
    mime_type: str
    width: int
    height: int
    duration: int | float
    fps: int | float
