from cmd import Cmd
from user import User
from storage import Storage

class AirbnbApp(Cmd):
    prompt = "Airbnb> "

    def do_register(self, username, password, role):
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role (owner/renter): ")
        user = User(username, password, role)

        data = Storage.load()
        data["users"].append(user.__dict__)
        Storage.save(data)
        print("Registration Successful!")

    def do_login(self, username, password):
        username = input("Username: ")
        password = input("Password: ")
        data = Storage.load()

        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                self.current_user = user
                print(f"Logged in as {username}")
        print("Invalid Credential")
    
    def do_add_house(self, username, role):
        if not hasattr(self, 'current_user') or self.current_user != "owner"
