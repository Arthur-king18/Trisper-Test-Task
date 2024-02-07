from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class _GetAuthorResponseSchema(BaseModel):
    id: int = Field(..., description="User ID")
    username: str = Field(..., description="Username")

class PublicationTopSchema(BaseModel):
    id: UUID = Field(..., description="ID")
    text: str = Field(..., description="Text")
    positive_votes: int = Field(..., description="Positive votes")
    negative_votes: int = Field(..., description="Negative votes")
    rating: int = Field(..., description="Rating")
    created_at: datetime = Field(..., description="Create at")
    author: _GetAuthorResponseSchema = Field(..., description="Author")

