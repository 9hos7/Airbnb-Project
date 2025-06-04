import cmd
from data_handlers.user import User
from storage import Storage
from data_handlers.house import House

class AirbnbApp(cmd.Cmd):
    # RECEIVING INPUT AND VALIDATING INPUT 
    prompt = "Airbnb "

    def do_register(self, args):
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role (owner/renter): ")
        user = User(username, password, role)

        data = Storage.load()
        data["users"].append(user.dict())
        Storage.save(data)
        print("Registration Successful!")

    def do_login(self, arg):
        username = input("Username: ")
        password = input("Password: ")
        data = Storage.load()

        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                self.current_user = user
                print(f"Logged in as {username}")
        print("Invalid Credential")
    
    def do_add_house(self, arg):
        if not hasattr(self, 'current_user') and self.current_user != "owner":
            print("Only logged-in owners can add house")
            return
        
        name = input("House Name: ")
        location = input("Location: ")
        room = input("Number of Rooms: ")
        price = float(input("Price: "))

        house = House(self.current_user["id"], name, location, room, price)
        house.validate_inputs()
        house.create()

        
    
    def do_delete_house(self, arg):
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
    
    def do_edit_house(self, arg):
        if not hasattr(self, 'current_user') and self.current_user.role != "owner":
            print("Only logged-in owners can edit house")
            return
        try:
            name = input("House Name: ")
            info = input("Which information do you want to edit? (name, location, room, price): ")
            info_type = ["name", "location", "room", "price"]
            if info not in info_type:
                raise KeyError("Invalid Prompt")
            change = input("What would you like to edit it to?: ")

            {
                "users": {},
            }

            stored_houses = Storage.load().get("house", {}).get()
        except KeyError as e:
            print(e)

    
    # def do_search(self, arg):
    #     if not hasattr(self, 'current_user') and self.current_user != "owner":
    #         print("Only logged-in owners can edit house")
    #         return
        
    #     location = input("Location to search: ")
    #     room = int(input("Minimum rooms: "))
    #     price = float(input("minimum_amount: "))

    #     data = Storage.load()
    #     if item in data:
    #         pass


if __name__ == "__main__":
    AirbnbApp().cmdloop