from fastapi import APIRouter, Request, Depends
from starlette.templating import Jinja2Templates

from app.events.router import get_events
from app.tickets.router import get_tickets
from app.users.router import authenticated_user

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/events")
async def get_events_page(
        request: Request,
        events=Depends(get_events),
        user=Depends(authenticated_user)
):
    return templates.TemplateResponse("events/events.html", {"request": request, "events": events, "user": user})


@router.get("/tickets")
async def get_tickets_page(
        request: Request,
        tickets=Depends(get_tickets),
        user=Depends(authenticated_user)
):
    return templates.TemplateResponse("tickets/tickets.html", {"request": request, "tickets": tickets, "user": user})


@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.get("/register")
async def get_register_page(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})
