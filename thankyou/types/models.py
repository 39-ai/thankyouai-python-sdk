from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

ModelT = TypeVar("ModelT", bound=str, covariant=True)
ParamsT = TypeVar("ParamsT", covariant=True)


@dataclass(frozen=True)
class ModelPricingOption:
    key: str
    label: str
    amount: float
    metadata: dict[str, object]


@dataclass(frozen=True)
class ModelPricing:
    category_key: str
    currency: str
    unit: str
    fallback: bool
    options: list[ModelPricingOption]


@dataclass(frozen=True)
class ModelSummary(Generic[ModelT]):
    id: ModelT
    display_name: str
    description: str
    operation: str
    category: str
    supported_modes: list[str]
    providers: list[str]
    vendor: str
    audio_support: str
    badges: list[str]
    features: list[str]
    preview_image: str
    pricing: ModelPricing | None = None


@dataclass(frozen=True)
class ModelDetail(ModelSummary[ModelT], Generic[ModelT, ParamsT]):
    default_mode: str = ""
    default_params: ParamsT | None = None
    input_schema: dict[str, object] | None = None
    primary_fields: list[dict[str, object]] | None = None
    advanced_fields: list[dict[str, object]] | None = None
    resolution_map: dict[str, object] | None = None


@dataclass(frozen=True)
class ModelListResponse(Generic[ModelT]):
    models: list[ModelSummary[ModelT]]
