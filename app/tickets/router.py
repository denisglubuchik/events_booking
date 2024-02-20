from fastapi import APIRouter, Depends

from fastapi_cache.decorator import cache
from pydantic import parse_obj_as

from app.tasks.tasks import send_ticket_confirmation_email
from app.users.models import Users
from app.users.router import current_user
from app.tickets.dao import TicketsDAO
from app.tickets.schemas import STickets

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.get("")
@cache(expire=60)
async def get_tickets(user: Users = Depends(current_user)) -> list[STickets]:
    tickets = await TicketsDAO.find_all(user_id=user.id)
    return tickets


@router.post("")
async def create_ticket(event_id: int, user: Users = Depends(current_user)):
    new_ticket = await TicketsDAO.create_new_ticket(event_id=event_id, user_id=user.id)
    ticket_dict = parse_obj_as(STickets, new_ticket).dict()

    # send_ticket_confirmation_email.delay(ticket_dict, user.email)
    return ticket_dict
