from typing import List
from fastapi import APIRouter, HTTPException, status, Path, Query

from app.config import SETTINGS
from app.models.scroll_model import Scroll
from app.services.core_service import CoreService


api_scroll = APIRouter()
core_service = CoreService()


@api_scroll.get('/', status_code=status.HTTP_200_OK)
async def get_scrolls() -> List[Scroll]:
    """Get a list of all scrolls.
    Args:
        None
    Returns:
        List[Scroll]: A list of scrolls.
    Raises:
        HTTPException: If an error occurs
    """
    scroll_list = []
    try:
        if not SETTINGS.APP_DEBUG:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail='Forbidden')

        # Get all scrolls
        scroll_list = core_service.get_scrolls()

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return scroll_list


@api_scroll.get('/{id}')
async def get_scroll(id: str = Path(title='Scroll document ID'), key: str = Query(default='')) -> Scroll:
    try:
        if not id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='id was not provided'
            )

        # Get a scroll by id
        scroll = core_service.get_scroll_by_id(id)
        if not scroll:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Scroll not found'
            )

        # Check expired_date
        if core_service.get_cur_ts() >= scroll.expired_at:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='The Scroll has already expired.'
            )

        # Check secret_key
        if scroll.secret_key and scroll.secret_key != key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Incorrect secret key.'
            )

        # Check read_once
        if scroll.read_once and scroll.has_been_read:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='The Scroll has already been read.'
            )

        # Update Scroll
        if not scroll.has_been_read:
            scroll.has_been_read = True
            affected_doc_count = core_service.update_scroll(
                id=id, scroll_model=scroll
            )
            if not affected_doc_count:
                raise Exception('No document updated')

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return scroll


@api_scroll.post('/')
async def post_scroll(scroll_model: Scroll) -> Scroll:
    try:
        if not scroll_model:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='scroll_model was not provided'
            )

        if not isinstance(scroll_model, Scroll):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail='scroll_model must be Scroll'
            )

        # Create a Scroll document
        created_scroll = core_service.create_scroll(scroll_model)

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return created_scroll
