"""Domain models for the gateway."""

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


class ItemRead(ItemCreate):
    id: int