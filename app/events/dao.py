from sqlalchemy import select
from app.dao.base import BaseDAO
from app.events.models import Events
from app.database import async_session_maker


class EventsDAO(BaseDAO):
    model = Events

    @classmethod
    async def find_events_by_location(cls, location, event_type):
        async with async_session_maker() as session:
            if event_type:
                query = select(cls.model).where(Events.location.like(f"%{location}%")).filter_by(event_type=event_type)
            else:
                query = select(cls.model).where(Events.location.like(f"%{location}%"))
            res = await session.execute(query)
            return res.scalars().all()
