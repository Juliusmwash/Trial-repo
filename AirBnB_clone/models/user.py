#!/usr/bin/python3
"""
module for class User
"""
from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """
    Contains the user details.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiates the class User.
        """
        super().__init__(*args, **kwargs)
