"""Ports (interfaces) for the storage service."""

from typing import Protocol
from src.domain.models import ItemRead


class ItemRepository(Protocol):
    """
    Contract for storing and retrieving items.
    The domain does not know HOW this is implemented.
    """
    def save(self, item: ItemRead) -> None:
        ...
    
    def get(self, item_id: int) -> ItemRead | None:
        ...