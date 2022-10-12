import urllib.parse
from typing import List
from bson import ObjectId

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

    def get(self) -> List[Scroll]:
        """Get docs from collection

        Returns:
            List[Scroll]: A list of Scroll documents
        """
        return [Scroll(**data) for data in self.coll.find()]

    def get_by_id(self, id: str) -> Scroll:
        """Get a doc from collection by its id

        Args:
            id (str): Document ID

        Returns:
            Scroll: Scroll document
        """
        if not id:
            return None

        # Query
        data = self.coll.find_one({'_id': ObjectId(id)})
        if not data:
            return None

        return Scroll(**data)

    def insert_one(self, scroll_model: Scroll) -> Scroll:
        """Insert a document from model

        Args:
            scroll_model (Scroll): Scroll

        Raises:
            ValueError: If scroll_model is not Scroll type

        Returns:
            Scroll: Scroll document
        """
        if not isinstance(scroll_model, Scroll):
            raise ValueError('scroll_model must be Scroll')

        inserted_data = self.coll.insert_one(document=scroll_model.dict())

        return self.get_by_id(id=inserted_data.inserted_id)

    def update_one(self, id: str, scroll_model: Scroll):
        """Update a document from model

        Args:
            id (str): Document ID
            scroll_model (Scroll): Scroll

        Raises:
            ValueError: If scroll_model is not Scroll type

        Returns:
            int: A number of documents affected
        """
        if not isinstance(scroll_model, Scroll):
            raise ValueError('scroll_model must be Scroll')

        # Filter out _id key
        no_id_scroll_data = {k: v for k,
                             v in scroll_model.dict().items() if k != '_id'}

        result = self.coll.update_one(
            filter={'_id': ObjectId(id)},
            update={'$set': no_id_scroll_data},
        )

        return result.modified_count
