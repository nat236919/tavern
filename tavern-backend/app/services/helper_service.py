import os
import hashlib
import random
import string
import secrets

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.config import SETTINGS


security = HTTPBasic()


class HelperService:
    """Helper Service
    """

    @staticmethod
    def generate_hex_string():
        """Generate Unique ID with 24 length

        Returns:
            str: ID
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=24))

    @staticmethod
    def generate_ticket_number():
        """Generate Ticket number using hashlib

        Returns:
            str: Ticket number (HEX string)
        """
        encoded_secret = SETTINGS.APP_SECRET_KEY.encode()
        salt = os.urandom(32)
        return hashlib.pbkdf2_hmac('sha256', encoded_secret, salt, 10000).hex()

    @staticmethod
    def is_cred_valid(credentials: HTTPBasicCredentials = Depends(security)) -> str:
        is_user_valid = secrets.compare_digest(
            credentials.username, SETTINGS.APP_ROOT_USER
        )
        is_password_valid = secrets.compare_digest(
            credentials.password, SETTINGS.APP_ROOT_PASSWORD
        )

        return is_user_valid and is_password_valid
