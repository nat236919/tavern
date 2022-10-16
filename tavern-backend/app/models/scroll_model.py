from time import time
from typing import Optional

from pydantic import BaseModel, Field

from app.services.helper_service import HelperService


################################################################################
# Scroll Model
# - Scroll
################################################################################
class Scroll(BaseModel):
    """Model for Scroll data

    Attrs:
        _id (str): Unique id. Defaults to HelperService.generate_hex_string().
        created_at (float): Date created of the scroll. Defaults to time.time()

        content (str): Content
        author (str): A name of the scroll creator
        expired_at (float): Expiration date for the scroll

        secret_key (Optional[str]): Secret to unlock content if applicable. Defaults to ''.
        read_once (Optional[bool]): Only allow be read once. Defaults to False.
        has_been_read (Optional[bool]): If this Scroll has already been read. Defaults to False.
    """
    # Auto-generated
    _id: str = Field(default_factory=HelperService.generate_hex_string())
    created_at: float = Field(default_factory=time)

    # Required
    content: str
    author: str
    expired_at: float

    # Optional
    secret_key: Optional[str] = ''
    read_once: Optional[bool] = False
    has_been_read: Optional[bool] = False
