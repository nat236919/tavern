"""
PROJECT: Tavern API
DESCRIPTION: This is the main file for the Tavern API.
AUTHOR: Nuttaphat Arunoprayoch
"""
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.middleware.cors import CORSMiddleware

from .config import SETTINGS
from .services.helper_service import HelperService
from .routers.api_scroll_router import api_scroll
from .routers.api_ticket_router import api_ticket


# Create the app
app = FastAPI(
    title=SETTINGS.APP_TITLE,
    description=SETTINGS.APP_DESCRIPTION,
    version=SETTINGS.APP_VERSION,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[SETTINGS.APP_URL],
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=['*'],
)


# Doc Routers
@app.get('/docs', include_in_schema=False)
async def get_documentation(is_cred_valid: bool = Depends(HelperService.is_cred_valid)):
    return get_swagger_ui_html(openapi_url='/openapi.json', title='docs')


@app.get('/redoc', include_in_schema=False)
async def get_redoc_documentation(is_cred_valid: bool = Depends(HelperService.is_cred_valid)):
    return get_redoc_html(openapi_url='/openapi.json', title='docs')


@app.get('/openapi.json', include_in_schema=False)
async def openapi(is_cred_valid: bool = Depends(HelperService.is_cred_valid)):
    if not is_cred_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Basic'},
        )
    return get_openapi(title=SETTINGS.APP_TITLE, version=SETTINGS.APP_VERSION, routes=app.routes)


# Register Routers
app.include_router(api_scroll, prefix='/scrolls', tags=['scroll_api'])
app.include_router(api_ticket, prefix='/tickets', tags=['ticket_api'])
