from uuid import UUID

from fastapi import APIRouter, Depends, Response, Request

from app.user.schemas import ExceptionResponseSchema
from app.vote.service import VoteService
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAuthenticated
)

vote_router = APIRouter()


@vote_router.post(
    "",
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def vote(
        request: Request,
        publication_id: UUID,
        is_positive_vote: bool,
) -> Response:
    await VoteService().vote(
        request=request,
        publication_id=publication_id,
        is_positive_vote=is_positive_vote
    )

    await VoteService().update_all_rating()

    return Response(status_code=200)

@vote_router.post(
    "/cancel",
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def cancel_vote(
        request: Request,
        publication_id: UUID,
) -> Response:
    await VoteService().cancel_vote(
        request=request,
        publication_id=publication_id,
    )

    await VoteService().update_all_rating()

    return Response(status_code=200)