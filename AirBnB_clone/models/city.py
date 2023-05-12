#!/usr/bin/python3
"""
Module for City class
"""
from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    """
    Contains city details
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instanciates class City
        """
        super().__init__(*args, **kwargs)
