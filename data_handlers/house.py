import uuid

from data_handlers.base import BaseDataHandler
from storage import Storage

class House(BaseDataHandler):
    def __init__(self, owner_id, name, location, rooms, price):
        super().__init__()
        self.owner_id = owner_id
        self.name = name
        self.location = location
        self.rooms = rooms
        self.price = price

    def validate_inputs(self):
        pass

    def create(self):
        data = Storage.load()
        data["house"].append(self.dict())
        Storage.save(data)
        print("House Added!")
        super().create()
    
    def update(self):
        pass