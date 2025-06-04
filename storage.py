import json
import os

class Storage:

    FILE = "storage/storage.json"

    @classmethod
    def save(cls, data):
        with open(cls.FILE, "w") as f:
            json.dump( data, f,  indent=4)

    def load(cls):
        if not os.path.exists(cls.FILE):
            return {"users": {}, "house": {}}
        with open(cls.FILE, 'r') as f:
            data = json.load(f)
        return data
