import time
from typing import Dict, List

from app.config import SETTINGS
from app.models.scroll_model import Scroll
from app.services.db_service import MongoService


class CoreService:
    """Core Service for API usage
    """

    def __init__(self) -> None:
        self.scroll_service = MongoService(
            db_name=SETTINGS.MONGO_DATABASE,
            coll_name=SETTINGS.MONGO_COLLECTION,
        )

    @staticmethod
    def get_cur_ts() -> int:
        """Get the current timestamp

        Returns:
            float: current timestamp (rounded)
        """
        return float(time.time())

    def get_scrolls(self) -> List[Scroll]:
        """Get all scrolls

        Returns:
            List[Scroll]: A list of scrolls
        """
        return self.scroll_service.get()

    def get_scroll_by_id(self, id) -> Scroll or Dict[None, None]:
        """Get scroll data by its id

        Args:
            id (str): uuid4

        Returns:
            Scroll: Scroll model
        """
        filtered_scroll_data_list = list(
            filter(lambda data: data.id == id, self.dummy_data_list)
        )

        if not filtered_scroll_data_list:
            return {}

        return filtered_scroll_data_list.pop()
