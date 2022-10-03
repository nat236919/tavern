from typing import List

import urllib.parse

from app.config import SETTINGS
from app.models.scroll_model import Scroll

from pymongo.mongo_client import MongoClient


class MongoService:
    """MongoDB Service
    """

    def __init__(self, db_name, coll_name) -> None:
        """Mongo DB service

        Args:
            db (str): DB name
            coll (str): Collection Name
        """
        self.db_name = db_name
        self.coll_name = coll_name
        self.root_username = urllib.parse.quote_plus(SETTINGS.MONGO_ROOT_USER)
        self.root_password = urllib.parse.quote_plus(
            SETTINGS.MONGO_ROOT_PASSWORD)

        self.mongo_client = MongoClient(
            f'mongodb://{self.root_username}:{self.root_password}@mongo:27017'
        )
        self.db = self.mongo_client[self.db_name]
        self.coll = self.db[self.coll_name]

    def get_collection_names(self) -> List[str]:
        """Get all collection names in DB

        Returns:
            List[str]: A list of collection names
        """
        return self.db.list_collection_names()

    def get(self):
        """Get docs from collection

        Returns:
            List[Scroll]: A list of Scroll documents
        """
        return [Scroll(**data) for data in self.coll.find()]
