from fastapi import APIRouter, Depends
from sqlalchemy.testing.pickleable import User

from fastapi_cache.decorator import cache

from app.events.dao import EventsDAO
from app.events.schemas import SEvents, EventTypeEnum, SEventsRead
from app.users.router import current_user

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.get("")
@cache(expire=60)
async def get_events(event_type: EventTypeEnum = None) -> list[SEventsRead]:
    if event_type:
        events = await EventsDAO.find_all(event_type=event_type)
    else:
        events = await EventsDAO.find_all()
    return events


@router.get("/{location}")
@cache(expire=60)
async def get_events_by_location(location: str, event_type: EventTypeEnum = None) -> list[SEventsRead]:
    events = await EventsDAO.find_events_by_location(location=location, event_type=event_type)
    return events


@router.get("/event/{event_id}")
async def get_event(event_id: int) -> SEventsRead:
    event = await EventsDAO.find_by_id(model_id=event_id)
    return event


@router.post("")
async def create_event(event: SEvents, user: User = Depends(current_user)):
    await EventsDAO.insert(
        title=event.title,
        description=event.description,
        location=event.location,
        event_type=event.event_type,
        price=event.price,
        date=event.date,
        people_amount=event.people_amount,
    )
