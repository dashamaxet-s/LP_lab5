"""In-memory implementation of ItemRepository."""

from src.domain.models import ItemRead
from src.domain.ports import ItemRepository


class InMemoryItemRepository(ItemRepository):
    """Stores items in a simple dictionary (in memory)."""
    
    def __init__(self) -> None:
        self._items: dict[int, ItemRead] = {}
        self._next_id: int = 1

    def save(self, item: ItemRead) -> None:
        self._items[item.id] = item

    def get(self, item_id: int) -> ItemRead | None:
        return self._items.get(item_id)

    def create(self, item_data: dict) -> ItemRead:
        """Helper to assign ID and save."""
        new_item = ItemRead(id=self._next_id, **item_data)
        self.save(new_item)
        self._next_id += 1
        return new_item