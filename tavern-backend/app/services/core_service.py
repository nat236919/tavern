import time
from typing import Dict, List

from app.config import SETTINGS
from app.models.scroll_model import Scroll
from app.models.ticket_model import Ticket
from app.services.db_service import MongoService


class CoreService:
    """Core Service for API usage
    """

    def __init__(self) -> None:
        self.ticket_service = MongoService(
            db_name=SETTINGS.MONGO_DATABASE,
            coll_name=SETTINGS.MONGO_TICKET_COLLECTION,
            model_template=Ticket,
        )
        self.scroll_service = MongoService(
            db_name=SETTINGS.MONGO_DATABASE,
            coll_name=SETTINGS.MONGO_COLLECTION,
            model_template=Scroll,
        )

    @staticmethod
    def get_cur_ts() -> int:
        """Get the current timestamp

        Returns:
            float: current timestamp (rounded)
        """
        return float(time.time())

    def get_ticket(self) -> Ticket:
        """Create and Insert Ticket

        Returns:
            Ticket: Ticket model
        """
        return self.ticket_service.insert_one(Ticket())

    def get_scrolls(self) -> List[Scroll]:
        """Get all scrolls

        Returns:
            List[Scroll]: A list of scrolls
        """
        return self.scroll_service.get()

    def get_scroll_by_id(self, id: str) -> Scroll:
        """Get scroll data by its id

        Args:
            id (str): HEX string

        Returns:
            Scroll: Scroll model
        """
        return self.scroll_service.get_by_id(id)

    def create_scroll(self, scroll_model: Scroll) -> Scroll:
        """Create a scroll data

        Args:
            scroll_model (Scroll): Scroll document

        Returns:
            Scroll: Scroll document
        """
        return self.scroll_service.insert_one(scroll_model)

    def update_scroll(self, id: str, scroll_model: Scroll) -> Scroll:
        """Update a scroll data

        Args:
            id (str): HEX string
            scroll_model (Scroll): Scroll document

        Returns:
            int: A number of documents affected
        """
        return self.scroll_service.update_one(id, scroll_model)
