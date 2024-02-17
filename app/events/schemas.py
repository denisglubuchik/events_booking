import enum
from datetime import date
from pydantic import BaseModel


class EventTypeEnum(enum.Enum):
    concert = "concert"
    museum = "museum"
    exhibition = "exhibition"
    other = "other"


class SEvents(BaseModel):
    id: int
    title: str
    description: str
    location: str
    event_type: EventTypeEnum
    price: int
    date: date
    people_amount: int

    class Config:
        from_attributes = True
