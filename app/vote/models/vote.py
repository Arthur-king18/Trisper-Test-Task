from sqlalchemy import Column, BigInteger, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from core.db import Base
from core.db.mixins import TimestampMixin


class Vote(Base, TimestampMixin):
    __tablename__ = "vote"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    positive_votes = Column(Boolean, default=False)
    negative_votes = Column(Boolean, default=False)

    user_id = Column(BigInteger, ForeignKey('user.id'))
    publication_id = Column(UUID(as_uuid=True), ForeignKey('publication.id'))


