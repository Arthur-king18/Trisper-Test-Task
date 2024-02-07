from typing import List

from fastapi import Request
from sqlalchemy import select, desc

from app.publication.models import Publication
from app.publication.schemas.publication import PublicationTopSchema
from app.user.services import UserService
from core.db import Transactional, session


class PublicationService:
    def __init__(self):
        ...

    async def get_top_publication(
        self,
        limit: int = 10,
    ) -> List[PublicationTopSchema]:
        top_publication = []

        query = select(Publication).order_by(desc(Publication.rating)).limit(limit)

        result = await session.execute(query)

        for publication in result.scalars().all():

            user = await UserService().get_user_by_user_id(user_id=publication.user_id)

            info = {
               "id": publication.id,
               "text": publication.text,
               "positive_votes": publication.positive_votes,
               "negative_votes": publication.negative_votes,
               "rating": publication.rating,
               "created_at": publication.created_at,
               "author": {
                   "id": user.id,
                   "username": user.username
               }
            }

            top_publication.append(info)

        return top_publication


    @Transactional()
    async def create_publication(
        self,
        request: Request,
        text: str,
    ) -> None:
        user = request.user

        publication = Publication(
            text=text,
            user_id=user.id
        )

        session.add(publication)