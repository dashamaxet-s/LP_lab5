"""HTTP client for calling the storage service."""

import httpx
from src.domain.models import ItemCreate, ItemRead
from src.domain.ports import StorageClientPort


class HttpStorageClient(StorageClientPort):
    """Adapter that calls the storage service via HTTP."""

    def __init__(self, base_url: str, timeout: float = 5.0) -> None:
        self.client = httpx.Client(base_url=base_url, timeout=timeout)

    def create_item(self, item: ItemCreate) -> ItemRead:
        resp = self.client.post("/items", json=item.model_dump())
        resp.raise_for_status()
        return ItemRead(**resp.json())

    def get_item(self, item_id: int) -> ItemRead | None:
        resp = self.client.get(f"/items/{item_id}")
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return ItemRead(**resp.json())