from fastapi import APIRouter

from api.user.v1.user import user_router as user_v1_router
from api.publication.v1.publication import publication_router as publication_v1_router
from api.publication.v1.vote.vote import vote_router as vote_v1_router
from api.auth.auth import auth_router
from api.constants import (
    USER_V1_API_PREFIX,
    AUTH_API_PREFIX,
    PUBLICATION_V1_API_PREFIX,
    VOTE_V1_API_PREFIX
)

router = APIRouter()

router.include_router(user_v1_router, prefix=USER_V1_API_PREFIX, tags=["User"])
router.include_router(publication_v1_router, prefix=PUBLICATION_V1_API_PREFIX, tags=["Publication"])
router.include_router(vote_v1_router, prefix=VOTE_V1_API_PREFIX, tags=["Vote"])
router.include_router(auth_router, prefix=AUTH_API_PREFIX, tags=["Auth"])


__all__ = ["router"]
