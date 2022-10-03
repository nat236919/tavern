from typing import List

import urllib.parse

from app.config import SETTINGS
from app.models.scroll_model import Scroll

from pymongo.mongo_client import MongoClient


class MongoService:
    """MongoDB Service
    """

    def __init__(self) -> None:
        self.root_username = urllib.parse.quote_plus(SETTINGS.MONGO_ROOT_USER)
        self.root_password = urllib.parse.quote_plus(
            SETTINGS.MONGO_ROOT_PASSWORD)
        self.database = SETTINGS.MONGO_DATABASE

        self.mongo_client = MongoClient(
            f'mongodb://{self.root_username}:{self.root_password}@mongo:27017'
        )
        self.db = self.mongo_client[self.database]

    def get_collection_names(self) -> List[str]:
        """Get all collection names in DB

        Returns:
            List[str]: A list of collection names
        """
        return self.db.list_collection_names()

    def execute(self, s):
        pass

    def get(self):
        pass

    def post(self):
        pass
