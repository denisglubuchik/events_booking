from pydantic import BaseModel
from datetime import date

from app.events.schemas import EventTypeEnum


class STickets(BaseModel):
    id: int
    event_id: int
    event_type: EventTypeEnum
    title: str
    user_id: int
    location: str
    date: date
    price: int
    created_date: date

    class Config:
        from_attributes = True
        use_enum_values = True

