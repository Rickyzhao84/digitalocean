from fastapi import FastAPI

from .services.service import EventService
from .routes.routing import get_router
from .repositories.repository import InMemoryRepository


repo = InMemoryRepository()
service = EventService(repo)

app = FastAPI(title="Event Ingestion Service")
app.include_router(get_router(service))


@app.get("/health")
def health():
    return {"status": "ok"}
