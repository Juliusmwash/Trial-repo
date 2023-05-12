#!/usr/bin/python3
"""
module for class Amenity
"""
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Stores the amenity details
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instanciates class Amenity
        """
        super().__init__(*args, **kwargs)
