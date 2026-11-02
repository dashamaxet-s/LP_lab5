"""API routes for the storage service."""

from fastapi import APIRouter, HTTPException
from src.domain.models import ItemCreate, ItemRead
from src.storage.repository import InMemoryItemRepository

router = APIRouter()

# Для простоты мы создаем репозиторий прямо здесь. 
# В идеале он должен внедряться через DI (мы сделаем это в main.py).
repo = InMemoryItemRepository()


@router.post("/items", response_model=ItemRead, status_code=201)
def create_item(item: ItemCreate) -> ItemRead:
    """Save a new item."""
    return repo.create(item.model_dump())


@router.get("/items/{item_id}", response_model=ItemRead)
def get_item(item_id: int) -> ItemRead:
    """Retrieve an item by ID."""
    item = repo.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item