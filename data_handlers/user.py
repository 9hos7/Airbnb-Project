import uuid

class User:
    def __init__(self, username, password, role):
        self.id = str(uuid.uuid4())
        self.username = username
        self.password = password
        self.role = role
        
#Role is either Owner or Renter

