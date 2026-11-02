"""Domain models for the storage service."""

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    """Data required to create a new item."""
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


class ItemRead(ItemCreate):
    """Item with an assigned ID."""
    id: int