"""API routes for the gateway."""
import httpx
from fastapi import APIRouter, HTTPException
from src.domain.models import ItemCreate, ItemRead
from src.domain.services import ItemService
from src.storage.client import HttpStorageClient
from src.config import get_settings

router = APIRouter()

# Сборка зависимостей (DI): берем настройки, создаем клиент и передаем в сервис
settings = get_settings()
storage_client = HttpStorageClient(
    base_url=settings.storage_url, 
    timeout=settings.timeout
)
item_service = ItemService(storage_client=storage_client)


@router.post("/items", response_model=ItemRead, status_code=201)
def create_item(item: ItemCreate) -> ItemRead:
    """Create item via storage service."""
    try:
        return item_service.create_item(item)
    except httpx.RequestError as e:
        # Ловим сетевые ошибки (сервер выключен, таймаут)
        print(f"Log: Storage is unavailable. Error: {e}")
        raise HTTPException(
            status_code=503, 
            detail="Storage service is temporarily unavailable"
        )


@router.get("/items/{item_id}", response_model=ItemRead)
def get_item(item_id: int) -> ItemRead:
    """Get item via storage service."""
    try:
        item = item_service.get_item(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    except httpx.RequestError as e:
        # Ловим сетевые ошибки
        print(f"Log: Storage is unavailable. Error: {e}")
        raise HTTPException(
            status_code=503, 
            detail="Storage service is temporarily unavailable"
        )