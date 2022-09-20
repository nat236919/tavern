import time
from typing import List

from config import SETTINGS
from models.scroll_model import Scroll


class CoreService:
    """Core Service for API usage
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_cur_ts() -> int:
        """Get the current timestamp

        Returns:
            float: current timestamp (rounded)
        """
        return float(time.time())

    def get_scrolls(self) -> List[Scroll]:
        return [
            Scroll(
                content='Dummy data',
                author='Admin',
                expired_at=self.get_cur_ts(),
            ),
            Scroll(
                content='Dummy data 2',
                author='Admin 2',
                expired_at=self.get_cur_ts(),
            )
        ]

    def get_scroll_by_id(self, id) -> Scroll:
        return Scroll(
            content='Dummy data',
            author='Admin',
        )
