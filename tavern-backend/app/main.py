"""
PROJECT: Tavern API
DESCRIPTION: This is the main file for the Tavern API.
AUTHOR: Nuttaphat Arunoprayoch
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import SETTINGS
from .routers.api_scroll_router import api_scroll
from .routers.api_ticket_router import api_ticket


# Create the app
app = FastAPI(
    title=SETTINGS.APP_TITLE,
    description=SETTINGS.APP_DESCRIPTION,
    version=SETTINGS.APP_VERSION,
)


# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[SETTINGS.APP_URL],
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=['*'],
)


# Register Routers
app.include_router(api_scroll, prefix='/scrolls', tags=['scroll_api'])
app.include_router(api_ticket, prefix='/tickets', tags=['ticket_api'])
