import os
from dotenv import load_dotenv

from pydantic import BaseSettings

load_dotenv()


class Config(BaseSettings):
    """Settings for the application."""

    # APP settings
    APP_VERSION: str = os.getenv('APP_VERSION')
    APP_TITLE: str = os.getenv('APP_TITLE')
    APP_DESCRIPTION: str = os.getenv('APP_DESCRIPTION')
    APP_URL: str = os.getenv('APP_URL')
    APP_PORT: int = os.getenv('APP_PORT')
    APP_DEBUG: bool = os.getenv('APP_DEBUG')
    APP_SECRET_KEY: str = os.getenv('APP_SECRET_KEY')

    # Mongo
    MONGO_ROOT_USER: str = os.getenv('MONGO_ROOT_USER')
    MONGO_ROOT_PASSWORD: str = os.getenv('MONGO_ROOT_PASSWORD')
    MONGO_DATABASE: str = os.getenv('MONGO_DATABASE')
    MONGO_COLLECTION: str = os.getenv('MONGO_COLLECTION')

    # Mongo Express
    MONGOEXPRESS_LOGIN: str = os.getenv('MONGOEXPRESS_LOGIN')
    MONGOEXPRESS_PASSWORD: str = os.getenv('MONGOEXPRESS_PASSWORD')


SETTINGS = Config()
