from uuid import UUID

from fastapi import Request
from sqlalchemy import update, delete, select

from app.publication.models import Publication
from app.vote.models import Vote
from core.db import Transactional, session
from core.exceptions import UserAlreadyVoteException


class VoteService:
    def __init__(self):
        ...

    async def vote(
            self,
            request: Request,
            publication_id: UUID,
            is_positive_vote: bool,
    ) -> None:
        if not await self.is_voted(publication_id, request.user.id):
            user = request.user

            await self.save_vote(
                publication_id=publication_id,
                is_positive_vote=is_positive_vote,
                user_id=user.id
            )

            await self.increase_vote_from_publication(
                publication_id=publication_id,
                is_positive_vote=is_positive_vote
            )

        else:
            raise UserAlreadyVoteException

    async def cancel_vote(
            self,
            request: Request,
            publication_id: UUID,
    ) -> None:
        is_positive_vote = await self.get_type_vote(
            publication_id=publication_id,
            user_id=request.user.id
        )

        await self.delete_vote_from_history(
            publication_id=publication_id,
            user_id=request.user.id
        )

        await self.decrease_vote_from_publication(
            publication_id=publication_id,
            is_positive_vote=is_positive_vote
        )

    @Transactional()
    async def update_all_rating(self):
        query = update(Publication).values(rating=Publication.positive_votes - Publication.negative_votes)

        await session.execute(query)

    @staticmethod
    async def is_voted(
            publication_id: UUID,
            user_id: int
    ) -> bool:
        """
        Сначала проверяю, голосовал ли когда-нибудь пользователь,
        а потом уже смотрю, голоовал ли имеенно за эту публикацию
        """
        voted = select(Vote).where(Vote.user_id == user_id)
        vote = await session.execute(voted)

        if vote.scalars().first() is None:
            return False

        else:
            query = select(Vote).where(Vote.publication_id == publication_id and Vote.user_id == user_id)
            result = await session.execute(query)

            return result.scalars().first() is not None

    @staticmethod
    @Transactional()
    async def save_vote(
            publication_id: UUID,
            is_positive_vote: bool,
            user_id: int
    ) -> None:
        if is_positive_vote:
            vote = Vote(
                publication_id=publication_id,
                user_id=user_id,
                positive_votes=is_positive_vote
            )

        else:
            vote = Vote(
                publication_id=publication_id,
                user_id=user_id,
                negative_votes=not is_positive_vote
            )

        session.add(vote)

    @staticmethod
    async def get_type_vote(
            publication_id: UUID,
            user_id: int
    ) -> bool:
        """
        True - проголосовал за
        False - прголосовал против
        """
        query = select(Vote).where(Vote.publication_id == publication_id and Vote.user_id == user_id)

        result = await session.execute(query)
        result = result.scalars().first()

        if result.positive_votes:
            return True

        else:
            return False

    @staticmethod
    @Transactional()
    async def delete_vote_from_history(
            publication_id: UUID,
            user_id: int
    ) -> None:

        query = delete(Vote).where(Vote.publication_id == publication_id and Vote.user_id == user_id)

        await session.execute(query)

    @staticmethod
    @Transactional()
    async def decrease_vote_from_publication(
            publication_id: UUID,
            is_positive_vote: bool
    ) -> None:

        if is_positive_vote:
            query = update(Publication).where(Publication.id == publication_id). \
                values(positive_votes=Publication.positive_votes - 1)

        else:
            query = update(Publication).where(Publication.id == publication_id). \
                values(negative_votes=Publication.negative_votes - 1)

        await session.execute(query)

    @staticmethod
    @Transactional()
    async def increase_vote_from_publication(
            publication_id: UUID,
            is_positive_vote: bool
    ) -> None:
        if is_positive_vote:
            query = update(Publication).where(Publication.id == publication_id). \
                values(positive_votes=Publication.positive_votes + 1)

        else:
            query = update(Publication).where(Publication.id == publication_id). \
                values(negative_votes=Publication.negative_votes + 1)

        await session.execute(query)
