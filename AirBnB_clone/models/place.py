#!/usr/bin/python3
"""
Module for class Place
"""
from models import storage
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Places details to be accessed from this class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """
        Instanciates Place class
        """
        super().__init__(*args, **kwargs)
