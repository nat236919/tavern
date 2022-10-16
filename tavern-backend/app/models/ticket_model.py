from time import time

from app.services.helper_service import HelperService

from pydantic import BaseModel, Field


################################################################################
# Token Model
# - Token
################################################################################
class Ticket(BaseModel):
    _id: str = Field(default_factory=HelperService.generate_hex_string())
    number: str = Field(default_factory=HelperService.generate_ticket_number())
    is_used: bool = False
    created_at: float = Field(default_factory=time)
