import uuid
import time
from typing import Optional

from pydantic import BaseModel, Field


################################################################################
# Scroll Model
# - Scroll
################################################################################
class Scroll(BaseModel):
    """Model for Scroll data

    Attrs:
        id (str): Unique id. Defaults to uuid.uuid4().
        created_at (int): Date created of the scroll. Defaults to time.time()
        content (str): Content
        author (str): A name of the scroll creator
        expired (int): Expiration date for the scroll
        secret_key (Optional[str]): Secret to unlock content if applicable. Defaults to ''.
        burn_when_open (Optional[bool]): Destroy the content when already open. Defaults to False.
    """
    # Auto-generated
    id: str = Field(default=uuid.uuid4())
    created_at: int = Field(default=int(time.time()))

    # Required
    content: str
    author: str
    expired_at: int

    # Optional
    secret_key: Optional[str] = ''
    burn_when_open: Optional[bool] = False
