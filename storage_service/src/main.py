"""Main entry point for the storage service."""

import uvicorn
from fastapi import FastAPI
from src.api.routes import router
from src.config import get_settings

# Создаем приложение
app = FastAPI(title="Storage Service", version="1.0.0")

# Подключаем роуты (наши эндпоинты /items)
app.include_router(router)


if __name__ == "__main__":
    # Читаем настройки из окружения (порт 8001)
    settings = get_settings()
    
    print(f"Starting Storage Service on port {settings.port}...")
    
    # Запускаем сервер
    uvicorn.run(
        "src.main:app", 
        host="127.0.0.1", 
        port=settings.port, 
        reload=True
    )