#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_id = kwargs.get("name", "")

