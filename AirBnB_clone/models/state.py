#!/usr/bin/python3
"""
Module for State class
"""
from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class that contains state data
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instanciates class State
        """
        super().__init__(*args, **kwargs)
