from fastapi import HTTPException
from starlette import status


class TicketException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class NoTicketsLeftException(TicketException):
    status_code = status.HTTP_409_CONFLICT
    detail = "No tickets left"


class EventHasPassedException(TicketException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Event has passed"
