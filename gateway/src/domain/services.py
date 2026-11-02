"""Business logic for the gateway."""

from src.domain.models import ItemCreate, ItemRead
from src.domain.ports import StorageClientPort

class ItemService:
    """Business logic for items. Depends only on the port, not on HTTP."""

    def __init__(self, storage_client: StorageClientPort) -> None:
        # Внедрение зависимости (DI): получаем клиент снаружи
        self._storage = storage_client

    def create_item(self, item_in: ItemCreate) -> ItemRead:
        """Create an item via the storage service."""
        # Здесь могла бы быть доп. логика (например, проверка прав)
        return self._storage.create_item(item_in)

    def get_item(self, item_id: int) -> ItemRead | None:
        """Retrieve an item."""
        return self._storage.get_item(item_id)