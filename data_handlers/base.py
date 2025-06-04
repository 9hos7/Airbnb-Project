import datetime
import uuid

from storage import Storage


class BaseDataHandler:
    def __init__(self):
        self.id = str(uuid.uuid4())

    def create(self, *args, **kwargs):
        # Logic to create or fine tune the data to be stored
        self.created_at = datetime.datetime.utcnow() 
        Storage.save(self.dict())

    def read(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        self.updated_at = datetime.datetime.utcnow()
        Storage.save(self.dict())

    def delete(self, *args, **kwargs):
        pass
