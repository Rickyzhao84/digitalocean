from typing import List, Protocol
from ..models.model import Event


class EventRepository(Protocol):
    def save(self, event: Event) -> Event:  # pragma: no cover - interface
        ...

    def list_all(self) -> List[Event]:  # pragma: no cover - interface
        ...

    def list_by_user(self, user_id: int) -> List[Event]:  # pragma: no cover - interface
        ...


class InMemoryRepository:
    def __init__(self) -> None:
        self._events: List[Event] = []

    def save(self, event: Event) -> Event:
        self._events.append(event)
        return event

    def list_all(self) -> List[Event]:
        return list(self._events)

    def list_by_user(self, user_id: int) -> List[Event]:
        return [e for e in self._events if e.user_id == user_id]


class PostgresRepository:
    """Placeholder for a Postgres-backed repository. Implement with SQLAlchemy when needed."""

    def __init__(self, db_session) -> None:
        self.session = db_session

    def save(self, event: Event) -> Event:
        raise NotImplementedError("PostgresRepository.save not implemented")

    def list_all(self) -> List[Event]:
        raise NotImplementedError("PostgresRepository.list_all not implemented")

    def list_by_user(self, user_id: int) -> List[Event]:
        raise NotImplementedError("PostgresRepository.list_by_user not implemented")
