#!/usr/bin/python3
"""
Module for class Review
"""
from models import storage
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class for reviews
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Instanciates class Review
        """
        super().__init__(*args, **kwargs)
