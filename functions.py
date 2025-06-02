from cmd import Cmd
from user import User
from storage import Storage
from house import House

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
    
    def add_house(self, name, location, room, price):
        if not hasattr(self, 'current_user') and self.current_user != "owner":
            print("Only logged-in owners can add house")
            return
        
        name = input("House Name: ")
        location = input("Location: ")
        room = input("Number of Rooms: ")
        price = float(input("Price: "))

        house = House(self.current_user["id"], name, location, room, price)

        data = Storage.load()
        data["house"].append(house.__dict__)
        Storage.save(data)
        print("House Added!")
    
    def delete_house(self, name):
        if not hasattr(self, 'current_user') and self.current_user != "owner":
            print("Only logged-in owners can delete house")
            return
        
        name = input("House Name: ")

        house = House(self.current_user["id"], name)

        data = Storage.load()
        
        for item in data["house"]:
            if house in item:
                return item
            item.clear
    
    def edit_house(self, info):
        if not hasattr(self, 'current_user') and self.current_user != "owner":
            print("Only logged-in owners can edit house")
            return
        
        name = input("House Name: ")
        info = input("Which information do you want to edit? (name, location, room, price): ")
        change = input("What would you like to edit it to?: ")

        house = House(self.current_user["id"], name)

        data = Storage.load()
        
        for item in data["house"]:
            if house in item:
                return item[info]
            item[info] = change
    
    def search(self):
        if not hasattr(self, 'current_user') and self.current_user != "owner":
            print("Only logged-in owners can edit house")
            return