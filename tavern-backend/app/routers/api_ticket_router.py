from fastapi import APIRouter, HTTPException, status, Path, Query

from app.config import SETTINGS
from app.models.ticket_model import Ticket
from app.services.core_service import CoreService


api_ticket = APIRouter()
core_service = CoreService()


@api_ticket.get('/single', response_model_include=('number', 'created_at'))
async def get_ticket() -> Ticket:
    try:
        # Get a Ticket
        ticket = core_service.get_ticket()
        if not ticket:
            raise Exception('No ticket created.')

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

    return ticket
