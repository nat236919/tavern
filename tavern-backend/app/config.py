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


SETTINGS = Config()
