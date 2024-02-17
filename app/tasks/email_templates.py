from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from app.config import settings
from pydantic import EmailStr
from app.qrcodes.qr import make_ticket_qr


def create_ticket_to_user(
        ticket: dict,
        email_to: EmailStr
):
    email = MIMEMultipart('alternative')
    email["Subject"] = "Подтверждение регистрации на мероприятие"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    img_path = make_ticket_qr(ticket)

    text = MIMEText(
        f"""
               <h1>Билет на меропритие</h1>
               <p>Вы регистрировались на {ticket["title"]}</p>
               <p>{ticket["location"]}</p>
               <p>{ticket["date"]}</p>
               <img src="cid:image">
            """, "html"
    )
    email.attach(text)

    image = MIMEImage(open(img_path, 'rb').read())

    image.add_header('Content-ID', '<image>')
    email.attach(image)

    return email
