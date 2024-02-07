import uuid

from sqlalchemy import Column, Unicode, BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.db import Base
from core.db.mixins import TimestampMixin


class Publication(Base, TimestampMixin):
    __tablename__ = "publication"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    text = Column(Unicode(2048), nullable=True)
    positive_votes = Column(BigInteger, default=0)
    negative_votes = Column(BigInteger, default=0)
    rating = Column(BigInteger, default=0)

    user_id = Column(BigInteger, ForeignKey('user.id'))

    user = relationship("User", back_populates="publication")
