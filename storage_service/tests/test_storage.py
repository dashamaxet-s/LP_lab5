"""Tests for storage service domain/repository."""

from src.storage.repository import InMemoryItemRepository


def test_create_item_in_repository() -> None:
    """Test that repository assigns an ID and saves the item."""
    repo = InMemoryItemRepository()
    
    # Создаем товар
    item = repo.create({"name": "Test Item", "price": 100.0})
    
    # Проверяем, что ID присвоился и данные верные
    assert item.id == 1
    assert item.name == "Test Item"
    assert item.price == 100.0


def test_get_missing_item() -> None:
    """Test that getting a non-existent item returns None."""
    repo = InMemoryItemRepository()
    item = repo.get(999)
    assert item is None