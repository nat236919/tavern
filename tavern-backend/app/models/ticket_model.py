from time import time

from app.services.helper_service import HelperService

from pydantic import BaseModel, Field


################################################################################
# Ticket Model
# - Ticket
################################################################################
class Ticket(BaseModel):
    """Model for Ticket data

    Attrs:
        _id (str): Unique id. Defaults to HelperService.generate_hex_string().
        number (int): Unique ticket number. Defaults to HelperService.generate_ticket_number().
        is_used (bool): Ticket usage indicator
        created_at (float): Date created of the scroll. Defaults to time.time()
    """
    _id: str = Field(default_factory=HelperService.generate_hex_string())
    number: str = Field(default_factory=HelperService.generate_ticket_number())
    is_used: bool = False
    created_at: float = Field(default_factory=time)
