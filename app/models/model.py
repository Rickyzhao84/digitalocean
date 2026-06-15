from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class EventIn(BaseModel):
	user_id: int = Field(..., gt=0)
	event_type: str = Field(..., min_length=1)
	timestamp: Optional[datetime] = None

	@validator("event_type")
	def event_type_must_not_be_empty(cls, v: str) -> str:
		if not v or not v.strip():
			raise ValueError("event_type must be a non-empty string")
		return v.strip()


class Event(EventIn):
	id: str
	timestamp: datetime

	class Config:
		orm_mode = True

