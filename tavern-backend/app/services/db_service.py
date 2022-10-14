import urllib.parse
from typing import Any, List
from bson import ObjectId

from app.config import SETTINGS

from pydantic import BaseModel
from pymongo.mongo_client import MongoClient


class MongoService:
    """MongoDB Service
    """

    def __init__(self, db_name, coll_name, model_template) -> None:
        """Mongo DB service

        Args:
            db (str): DB name
            coll (str): Collection Name
            model_template (BaseModel): pydantic BaseModel
        """
        self.db_name = db_name
        self.coll_name = coll_name
        self.model_template = model_template
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

    def get(self) -> List[BaseModel]:
        """Get docs from collection

        Returns:
            List[BaseModel]: A list of BaseModel documents
        """
        return [self.model_template(**data) for data in self.coll.find()]

    def get_by_id(self, id: str) -> BaseModel:
        """Get a doc from collection by its id

        Args:
            id (str): Document ID

        Raises:
            ValueError: id parameter is not a string whose length is 24

        Returns:
            BaseModel: BaseModel document
        """
        if isinstance(id, str) and len(id) != 24:
            raise ValueError('id must be 24 in length.')

        # Query
        data = self.coll.find_one({'_id': ObjectId(id)})
        if not data:
            return None

        return self.model_template(**data)

    def get_by_key_value(self, key: str, value: Any) -> BaseModel:
        """Get a doc from collection by its unique key

        Args:
            key (str): Document key
            values (Any): Document value

        Returns:
            BaseModel: BaseModel document
        """
        # Query
        data = self.coll.find_one({key: value})
        if not data:
            return None

        return self.model_template(**data)

    def insert_one(self, model_data: BaseModel) -> BaseModel:
        """Insert a document from model

        Args:
            model_data (BaseModel): pydantic BaseModel

        Raises:
            ValueError: If model_data is not BaseModel type

        Returns:
            BaseModel: BaseModel document
        """
        if not isinstance(model_data, self.model_template):
            raise ValueError('model_data must be BaseModel')

        inserted_data = self.coll.insert_one(document=model_data.dict())

        return self.get_by_id(id=str(inserted_data.inserted_id))

    def update_one(self, id: str, model_data: BaseModel) -> int:
        """Update a document from model

        Args:
            id (str): Document ID
            model_data (BaseModel): pydantic BaseModel

        Raises:
            ValueError: id parameter is not a string whose length is 24
            ValueError: If model_data is not BaseModel type

        Returns:
            int: A number of documents affected
        """
        if isinstance(id, str) and len(id) != 24:
            raise ValueError('id must be 24 in length.')

        if not isinstance(model_data, self.model_template):
            raise ValueError('model_data must be BaseModel')

        result = self.coll.update_one(
            filter={'_id': ObjectId(id)},
            update={
                '$set': {
                    k: v for k, v in model_data.dict().items() if k != '_id'
                }
            },
        )

        return result.modified_count

    def update_one_by_kay_value(self, key: str, value: Any, model_data: BaseModel) -> int:
        """Update a document by its key and value

        Args:
            key (str): Document key
            values (Any): Document value
            model_data (BaseModel): pydantic BaseModel

        Raises:
            ValueError: id parameter is not a string whose length is 24
            ValueError: If model_data is not BaseModel type

        Returns:
            int: A number of documents affected
        """
        if not isinstance(model_data, self.model_template):
            raise ValueError('model_data must be BaseModel')

        result = self.coll.update_one(
            filter={key: value},
            update={
                '$set': {
                    k: v for k, v in model_data.dict().items() if k != '_id'
                }
            },
        )

        return result.modified_count
