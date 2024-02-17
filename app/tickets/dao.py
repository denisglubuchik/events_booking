from sqlalchemy import select, func, insert
from datetime import datetime, date

from app.dao.base import BaseDAO
from app.events.models import Events
from app.tickets.models import Tickets
from app.database import async_session_maker
from app.exceptions import NoTicketsLeftException, EventHasPassedException


class TicketsDAO(BaseDAO):
    model = Tickets

    @classmethod
    async def create_new_ticket(cls, event_id: int, user_id: int):
        try:
            async with async_session_maker() as session:
                query = select(Events.date).filter_by(id=event_id)
                event_date: date = await session.execute(query)
                event_date = event_date.scalar()
                if event_date < datetime.utcnow().date():
                    raise EventHasPassedException
                tickets_booked = (
                    select(Tickets)
                    .where(Tickets.event_id == event_id)
                    .cte("tickets_booked")
                )
                get_tickets_left = (
                    select(Events.people_amount - func.count(tickets_booked.c.id)).select_from(Events)
                    .join(tickets_booked, tickets_booked.c.event_id == Events.id, isouter=True)
                    .where(Events.id == event_id)
                    .group_by(Events.people_amount, tickets_booked.c.event_id)
                )

                tickets_left = await session.execute(get_tickets_left)
                tickets_left: int = tickets_left.scalar()

                if tickets_left > 0:
                    event = select(Events).filter_by(id=event_id)
                    event = await session.execute(event)
                    event = event.scalars().one()
                    add_ticket = insert(Tickets).values(
                        event_id=event_id,
                        user_id=user_id,
                        event_type=event.event_type,
                        title=event.title,
                        location=event.location,
                        date=event.date,
                        price=event.price,
                    ).returning(Tickets)

                    new_ticket = await session.execute(add_ticket)
                    await session.commit()
                    return new_ticket.scalars().one()
                else:
                    raise NoTicketsLeftException
        except EventHasPassedException:
            raise EventHasPassedException
        except NoTicketsLeftException:
            raise NoTicketsLeftException

