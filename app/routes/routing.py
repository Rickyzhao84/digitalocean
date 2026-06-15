from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from ..models.model import EventIn, Event
from ..services.service import EventService


def get_router(service: EventService) -> APIRouter:
	router = APIRouter()

	@router.post("/events", response_model=Event, status_code=status.HTTP_201_CREATED)
	def post_event(payload: EventIn):
		# Route only handles HTTP layer and delegates business logic to service
		return service.create_event(payload)

	@router.get("/stats")
	def stats():
		return service.get_stats()

	@router.get("/users/{user_id}/events", response_model=List[Event])
	def user_events(user_id: int):
		events = service.get_events_for_user(user_id)
		return events

	return router

