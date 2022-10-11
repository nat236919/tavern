import random
import string
from time import time
from typing import Optional

from pydantic import BaseModel, Field


################################################################################
# Scroll Model
# - Scroll
################################################################################
def generate_hex_string():
    """Generate Unique ID with 24 length

    Returns:
        str: ID
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=24))


class Scroll(BaseModel):
    """Model for Scroll data

    Attrs:
        _id (str): Unique id. Defaults to ).
        created_at (float): Date created of the scroll. Defaults to time.time()
        content (str): Content
        author (str): A name of the scroll creator
        expired_at (float): Expiration date for the scroll
        secret_key (Optional[str]): Secret to unlock content if applicable. Defaults to ''.
        read_once (Optional[bool]): Only allow be read once. Defaults to False.
    """
    # Auto-generated
    _id: str = Field(default_factory=generate_hex_string)
    created_at: float = Field(default_factory=time)

    # Required
    content: str
    author: str
    expired_at: float

    # Optional
    secret_key: Optional[str] = ''
    read_once: Optional[bool] = False
