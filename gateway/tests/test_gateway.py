"""Tests for gateway domain logic."""

from src.domain.models import ItemCreate, ItemRead
from src.domain.services import ItemService


class FakeStorageClient:
    """
    Фальшивый клиент склада (Mock).
    Он не делает сетевых запросов, а просто хранит данные в памяти.
    """
    def __init__(self) -> None:
        self._items: dict[int, ItemRead] = {}
        self._next_id = 1

    def create_item(self, item: ItemCreate) -> ItemRead:
        new_item = ItemRead(id=self._next_id, **item.model_dump())
        self._items[self._next_id] = new_item
        self._next_id += 1
        return new_item

    def get_item(self, item_id: int) -> ItemRead | None:
        return self._items.get(item_id)


def test_service_create_item() -> None:
    """Test domain service creating an item using the fake client."""
    # Внедряем зависимость (мок) в наш сервис
    fake_client = FakeStorageClient()
    service = ItemService(storage_client=fake_client)
    
    item_in = ItemCreate(name="Gateway Test", price=50.0)
    result = service.create_item(item_in)
    
    assert result.id == 1
    assert result.name == "Gateway Test"


def test_service_get_item() -> None:
    """Test domain service getting an item using the fake client."""
    fake_client = FakeStorageClient()
    service = ItemService(storage_client=fake_client)
    
    # Сначала создаем, потом ищем
    service.create_item(ItemCreate(name="Find Me", price=10.0))
    result = service.get_item(1)
    
    assert result is not None
    assert result.name == "Find Me"