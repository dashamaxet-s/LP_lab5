"""Main entry point for the gateway service."""

import uvicorn
from fastapi import FastAPI
from src.api.routes import router
from src.config import get_settings

app = FastAPI(title="API Gateway", version="1.0.0")
app.include_router(router)

if __name__ == "__main__":
    settings = get_settings()
    print(f"Starting API Gateway on port {settings.port}...")
    uvicorn.run(
        "src.main:app", 
        host="127.0.0.1", 
        port=settings.port, 
        reload=True
    )