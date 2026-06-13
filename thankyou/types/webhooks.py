from __future__ import annotations

from dataclasses import dataclass, field

from .generations import GenerationResponse


@dataclass(frozen=True)
class ThankYouWebhookEvent:
    event: str
    generation: GenerationResponse[str, object, object] | None = None
    data: dict[str, object] = field(default_factory=dict)
