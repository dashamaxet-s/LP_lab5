"""Ports for the gateway domain."""

from typing import Protocol
from src.domain.models import ItemCreate, ItemRead


class StorageClientPort(Protocol):
    """Interface for calling the external storage service."""
    
    def create_item(self, item: ItemCreate) -> ItemRead:
        ...
        
    def get_item(self, item_id: int) -> ItemRead | None:
        ...