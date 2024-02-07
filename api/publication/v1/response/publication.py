from pydantic import BaseModel, Field


class PublicationResponse(BaseModel):
    text: str = Field(..., description="Text")
