from pydantic import EmailStr
import smtplib

from app.config import settings
from app.tasks._celery import celery
from app.tasks.email_templates import create_ticket_to_user


@celery.task
def send_ticket_confirmation_email(
        ticket: dict,
        email_to: EmailStr
):
    email_to_mock = settings.SMTP_USER
    msg_content = create_ticket_to_user(ticket, email_to_mock)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
