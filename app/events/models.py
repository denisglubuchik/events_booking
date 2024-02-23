from sqlalchemy import Column, Integer, String, Date, Enum
from app.database import Base
from app.events.schemas import EventTypeEnum


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    location = Column(String, nullable=False)
    event_type = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    people_amount = Column(Integer, nullable=False)