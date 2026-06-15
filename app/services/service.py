from typing import List, Dict
from ..models.model import EventIn, Event
from datetime import datetime
import uuid
from ..repositories.repository import EventRepository


class EventService:
    """Business logic for events; persistence delegated to a repository."""

    def __init__(self, repo: EventRepository) -> None:
        self._repo = repo

    def create_event(self, payload: EventIn) -> Event:
        ts = payload.timestamp or datetime.utcnow()
        ev = Event(
            id=str(uuid.uuid4()),
            user_id=payload.user_id,
            event_type=payload.event_type,
            timestamp=ts,
        )
        return self._repo.save(ev)

    def get_stats(self) -> Dict:
        events = self._repo.list_all()
        total = len(events)
        by_type: Dict[str, int] = {}
        for e in events:
            by_type[e.event_type] = by_type.get(e.event_type, 0) + 1
        return {"total_events": total, "events_by_type": by_type}

    def get_events_for_user(self, user_id: int) -> List[Event]:
        filtered = self._repo.list_by_user(user_id)
        # newest first
        return sorted(filtered, key=lambda e: e.timestamp, reverse=True)

