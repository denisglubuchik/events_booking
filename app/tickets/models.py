from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, Date, String, Enum
from app.database import Base
from app.events.schemas import EventTypeEnum


class Tickets(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    event_id = Column(ForeignKey("events.id"))
    event_type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    user_id = Column(ForeignKey("users.id"))
    location = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    created_date = Column(Date, default=datetime.utcnow)