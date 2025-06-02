import json
import os

class Storage:

    FILE = "storage/storage.json"

    def save(cls, data):
        with open(cls.FILE, "w") as f:
            json.dump( data, f,  indent=4)

    def load(cls):
        if not os.path.exists:
            return {"users": [], "house": []}
        with open(cls.FILE, 'r') as f:
            json.load(f)

