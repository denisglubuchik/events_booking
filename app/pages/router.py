from fastapi import APIRouter, Request, Depends
from starlette.templating import Jinja2Templates

from app.events.router import get_events
from app.tickets.router import get_tickets

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/events")
async def get_events_page(request: Request, events=Depends(get_events)):
    return templates.TemplateResponse("events/events.html", {"request": request, "events": events})


@router.get("/tickets")
async def get_tickets_page(request: Request, tickets=Depends(get_tickets)):
    return templates.TemplateResponse("tickets/tickets.html", {"request": request, "tickets": tickets})
