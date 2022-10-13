import os
import random
import string
import hashlib
from time import time

from app.config import SETTINGS

from pydantic import BaseModel, Field


################################################################################
# Token Model
# - Token
################################################################################
def generate_hex_string():
    """Generate Unique ID with 24 length

    Returns:
        str: ID
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=24))


def generate_ticket_number():
    """Generate Ticket number using hashlib

    Returns:
        str: Ticket number (HEX string)
    """
    encoded_secret = SETTINGS.APP_SECRET_KEY.encode()
    salt = os.urandom(32)
    return hashlib.pbkdf2_hmac('sha256', encoded_secret, salt, 10000).hex()


class Ticket(BaseModel):
    _id: str = Field(default_factory=generate_hex_string)
    created_at: float = Field(default_factory=time)
    number: str = Field(default_factory=generate_ticket_number)
    is_used: bool = False
