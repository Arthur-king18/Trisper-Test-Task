from typing import List

from fastapi import APIRouter, Depends, Request, Query

from api.publication.v1.response.publication import PublicationResponse
from app.publication.schemas.publication import PublicationTopSchema
from app.publication.service import PublicationService
from app.user.schemas import ExceptionResponseSchema
from core.exceptions import PublicationTooBigException
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAuthenticated
)

publication_router = APIRouter()


@publication_router.get(
    "",
    response_model=List[PublicationTopSchema],
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def get_top_publication(
    limit: int = Query(10, description="Limit")
) -> List[PublicationTopSchema]:

    return await PublicationService().get_top_publication(limit=limit)


@publication_router.post(
    "",
    response_model=PublicationResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def create_publication(request: Request, text: str) -> PublicationResponse:
    if len(text) <= 2048:
        await PublicationService().create_publication(text=text, request=request)

    else:
        raise PublicationTooBigException

    return {"text": text}
