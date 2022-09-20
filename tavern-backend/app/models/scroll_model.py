from uuid import uuid4
from time import time
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
        created_at (float): Date created of the scroll. Defaults to time.time()
        content (str): Content
        author (str): A name of the scroll creator
        expired_at (float): Expiration date for the scroll
        secret_key (Optional[str]): Secret to unlock content if applicable. Defaults to ''.
        burn_when_open (Optional[bool]): Destroy the content when already open. Defaults to False.
    """
    # Auto-generated
    id: str = Field(default_factory=uuid4)
    created_at: float = Field(default_factory=time)

    # Required
    content: str
    author: str
    expired_at: float

    # Optional
    secret_key: Optional[str] = ''
    burn_when_open: Optional[bool] = False
