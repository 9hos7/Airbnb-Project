import uuid

class House:
    def __init__(self, owner_id, name, location, rooms, price):
        self.id = str(uuid.uuid4())
        self.owner_id = owner_id
        self.name = name
        self.location = location
        self.rooms = rooms
        self.price = price
        