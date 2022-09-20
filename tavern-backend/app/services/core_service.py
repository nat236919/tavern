import time
from typing import Dict, List

from config import SETTINGS
from models.scroll_model import Scroll


class CoreService:
    """Core Service for API usage
    """

    def __init__(self) -> None:
        self.dummy_data_list = [
            Scroll(
                content='Dummy data',
                author='Admin',
                expired_at=self.get_cur_ts(),
            ),
            Scroll(
                content='Dummy data 2',
                author='Admin 2',
                expired_at=self.get_cur_ts(),
            ),
            Scroll(
                id='e5f70ca4-3d0f-40a9-9de7-328ffd85f03d',
                content='Dummy data 3',
                author='Admin 3',
                expired_at=self.get_cur_ts(),
            )
        ]

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
        return self.dummy_data_list

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
