# Architecture of the Microservices System

## 1. Interaction Diagram

```text
       [ Client (Swagger / curl) ]
                   |
                   | HTTP (POST /items, GET /items/1)
                   v
       +-----------------------+
       |    API Gateway        | (Port 8000)
       |  (api -> domain)      |
       +-----------------------+
                   |
                   | HTTP (httpx)
                   v
       +-----------------------+
       |    Storage Service    | (Port 8001)
       |  (api -> domain ->    |
       |        storage)       |
       +-----------------------+
                   |
                   v
           [ In-Memory Dict ]
```

## 2. Description of Layers

Both services follow a strict layered architecture (`api` -> `domain` -> `storage`):

### Storage Service (Port 8001)
*   **`api/`**: FastAPI routers, Pydantic schemas for requests/responses.
*   **`domain/`**: Contains `models.py` and `ports.py` (the `ItemRepository` Protocol).
*   **`storage/`**: Contains `repository.py`, the concrete implementation of the port (in-memory dictionary).

### API Gateway (Port 8000)
*   **`api/`**: FastAPI routers.
*   **`domain/`**: Contains `models.py`, `ports.py` (the `StorageClientPort` Protocol), and `services.py` (business logic).
*   **`storage/`**: Contains `client.py`, which is an adapter (HTTP client using `httpx`) that implements the port.

## 3. Justification of Service Boundaries

**Why split into two services?**
*   **Separation of Concerns**: The Gateway handles external requests, validation, and orchestration. The Storage Service handles data persistence.
*   **Scalability**: If the Storage Service gets overloaded, we can scale it independently without affecting the Gateway.
*   **Isolation**: If the Storage Service goes down, the Gateway catches the error (via `httpx.RequestError`) and returns `503 Service Unavailable` instead of crashing.

**Where is data stored?**
*   Data is stored in the Storage Service in an in-memory dictionary (`InMemoryItemRepository`). It acts as the single source of truth.

**How are contracts agreed upon?**
*   Contracts are agreed upon using Pydantic models (`ItemCreate`, `ItemRead`). Both services share identical models to ensure seamless JSON serialization/deserialization over HTTP.