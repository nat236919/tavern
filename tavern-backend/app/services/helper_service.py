import os
import hashlib
import random
import string

from app.config import SETTINGS


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
