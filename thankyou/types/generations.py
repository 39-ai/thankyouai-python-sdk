from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Generic, Literal, TypeVar

GenerationStatus = Literal[
    "pending",
    "queued",
    "processing",
    "running",
    "completed",
    "succeeded",
    "failed",
    "cancelled",
    "partial_success",
]

ModelT = TypeVar("ModelT", bound=str, covariant=True)
OutputT = TypeVar("OutputT", covariant=True)
ParamsT = TypeVar("ParamsT", covariant=True)


@dataclass(frozen=True)
class UsageResponse:
    credits_consumed: float
    currency: str


@dataclass(frozen=True)
class GenerationFieldError:
    field: list[str | int]
    type: str
    message: str
    constraint: dict[str, object] | None = None


@dataclass(frozen=True)
class GenerationErrorDetails:
    trace_ref: str | None = None
    request_id: str | None = None
    category: str | None = None
    field_errors: list[GenerationFieldError] | None = None


@dataclass(frozen=True)
class GenerationErrorBody:
    code: str
    type: str
    message: str
    retryable: bool
    details: GenerationErrorDetails | dict[str, object] | None = None


@dataclass(frozen=True)
class GenerationResponse(Generic[ModelT, OutputT, ParamsT]):
    id: str
    status: GenerationStatus
    model: ModelT
    output: list[OutputT]
    error: GenerationErrorBody | None
    usage: UsageResponse
    progress: float
    params_raw: ParamsT
    resolved_params: ParamsT
    created_at: datetime
    submitted_model: str | None = None
    started_at: datetime | None = None
    finished_at: datetime | None = None
    retried_from: str | None = None


@dataclass(frozen=True)
class GenerationStatusResponse:
    id: str
    status: GenerationStatus
    progress: float
    finished_at: datetime | None = None


@dataclass(frozen=True)
class QuoteResponse(Generic[ModelT, ParamsT]):
    quote_id: str
    model: ModelT
    estimated_cost: float
    currency: str
    blocking_reasons: list[str]
    resolved_params: ParamsT
    expires_at: datetime


@dataclass(frozen=True)
class GenerationListResponse(Generic[ModelT, OutputT, ParamsT]):
    generations: list[GenerationResponse[ModelT, OutputT, ParamsT]]
    total: int
    page: int
    page_size: int
