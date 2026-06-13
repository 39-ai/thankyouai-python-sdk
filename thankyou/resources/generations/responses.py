from __future__ import annotations

from collections.abc import Mapping
from typing import TypeVar, cast

from thankyou._utils import as_dict, parse_datetime, parse_optional_datetime
from thankyou.types import (
    GenerationErrorBody,
    GenerationErrorDetails,
    GenerationFieldError,
    GenerationListResponse,
    GenerationResponse,
    GenerationStatus,
    GenerationStatusResponse,
    QuoteResponse,
    UsageResponse,
)

ModelT = TypeVar("ModelT", bound=str)
OutputT = TypeVar("OutputT")
ParamsT = TypeVar("ParamsT")


def parse_usage(value: object) -> UsageResponse:
    data = as_dict(value)
    return UsageResponse(
        credits_consumed=float(data.get("credits_consumed", 0)),
        currency=str(data.get("currency", "")),
    )


def parse_error(value: object) -> GenerationErrorBody | None:
    if value is None:
        return None
    data = as_dict(value)
    details = data.get("details")
    parsed_details: GenerationErrorDetails | dict[str, object] | None
    if isinstance(details, Mapping):
        field_errors = details.get("field_errors")
        parsed_field_errors = [
            GenerationFieldError(
                field=list(as_dict(item).get("field", [])),
                type=str(as_dict(item).get("type", "")),
                message=str(as_dict(item).get("message", "")),
                constraint=cast(dict[str, object] | None, as_dict(item).get("constraint")),
            )
            for item in field_errors
            if isinstance(item, Mapping)
        ] if isinstance(field_errors, list) else None
        parsed_details = GenerationErrorDetails(
            trace_ref=cast(str | None, details.get("trace_ref")),
            request_id=cast(str | None, details.get("request_id")),
            category=cast(str | None, details.get("category")),
            field_errors=parsed_field_errors,
        )
    else:
        parsed_details = cast(dict[str, object] | None, details)
    return GenerationErrorBody(
        code=str(data.get("code", "")),
        type=str(data.get("type", "")),
        message=str(data.get("message", "")),
        retryable=bool(data.get("retryable", False)),
        details=parsed_details,
    )


def parse_generation_response(
    response: object,
) -> GenerationResponse[ModelT, OutputT, ParamsT]:
    data = as_dict(response)
    return GenerationResponse(
        id=str(data["id"]),
        status=cast(GenerationStatus, data["status"]),
        model=cast(ModelT, data["model"]),
        submitted_model=cast(str | None, data.get("submitted_model")),
        output=cast(list[OutputT], data.get("output", [])),
        error=parse_error(data.get("error")),
        usage=parse_usage(data.get("usage", {})),
        progress=float(data.get("progress", 0)),
        params_raw=cast(ParamsT, data.get("params_raw", {})),
        resolved_params=cast(ParamsT, data.get("resolved_params", {})),
        created_at=parse_datetime(cast(str, data["created_at"])),
        started_at=parse_optional_datetime(cast(str | None, data.get("started_at"))),
        finished_at=parse_optional_datetime(cast(str | None, data.get("finished_at"))),
        retried_from=cast(str | None, data.get("retried_from")),
    )


def parse_generation_status_response(response: object) -> GenerationStatusResponse:
    data = as_dict(response)
    return GenerationStatusResponse(
        id=str(data["id"]),
        status=cast(GenerationStatus, data["status"]),
        progress=float(data.get("progress", 0)),
        finished_at=parse_optional_datetime(cast(str | None, data.get("finished_at"))),
    )


def parse_generation_list_response(
    response: object,
) -> GenerationListResponse[ModelT, OutputT, ParamsT]:
    data = as_dict(response)
    return GenerationListResponse(
        generations=[
            parse_generation_response(item)
            for item in cast(list[object], data.get("generations", []))
        ],
        total=int(data.get("total", 0)),
        page=int(data.get("page", 0)),
        page_size=int(data.get("page_size", 0)),
    )


def parse_quote_response(response: object) -> QuoteResponse[ModelT, ParamsT]:
    data = as_dict(response)
    return QuoteResponse(
        quote_id=str(data["quote_id"]),
        model=cast(ModelT, data["model"]),
        estimated_cost=float(data.get("estimated_cost", 0)),
        currency=str(data.get("currency", "")),
        blocking_reasons=[str(reason) for reason in data.get("blocking_reasons", [])],
        resolved_params=cast(ParamsT, data.get("resolved_params", {})),
        expires_at=parse_datetime(cast(str, data["expires_at"])),
    )
