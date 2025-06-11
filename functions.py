import cmd
from data_handlers.user import User
from storage import Storage
from data_handlers.house import House

class AirbnbApp(cmd.Cmd):
    # RECEIVING INPUT AND VALIDATING INPUT 
    prompt = "Airbnb > "

    def __init__(self):
        super().__init__()
        self.current_user = None

    def do_register(self, arg=None):
        """Register a new user"""
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role (owner/renter): ").lower()

        user = User(username, password, role)
        data = Storage.load()

        # Ensure 'users' is a dict
        users = data.get("users", {})
        if username in users:
            print("User already exists!")
            return

        users[username] = user.__dict__
        data["users"] = users
        Storage.save(data)

        print("Registration Successful!")

    def do_login(self, arg=None):
        """Log in a user"""
        username = input("Username: ")
        password = input("Password: ")

        data = Storage.load()
        users = data.get("users", {})

        user = users.get(username)
        if user and user["password"] == password:
            self.current_user = user
            print(f"Logged in as {username}")
        else:
            print("Invalid credentials.")
    
    def do_add_house(self, arg=None):
        """Add a house (owners only)"""
        if not self.current_user or self.current_user['role'] != "owner":
            print("Only logged-in owners can add houses.")
            return

        name = input("House Name: ")
        location = input("Location: ")
        room = input("Number of Rooms: ")
        while True:
            price_input = input("Price: ").strip()
            if "$" in price_input:
                print("Please enter the price as a number without the '$' symbol.")
                continue
            try:
                price = float(price_input)
                break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")


        house = House(self.current_user["id"], name, location, room, price)

        data = Storage.load()
        houses = data.get("house", {})
        houses[house.id] = house.__dict__  # Or house.dict() if you defined one
        data["house"] = houses
        Storage.save(data)

        print("House added successfully.")

        
    
    def do_delete_house(self, arg=None):
        """Delete a house by name (owners only)"""
        if not self.current_user or self.current_user['role'] != "owner":
            print("Only logged-in owners can delete houses.")
            return

        name = input("House Name to delete: ")
        data = Storage.load()
        houses = data.get("house", {})

        to_delete = None
        for house_id, h in houses.items():
            if h["owner_id"] == self.current_user["id"] and h["name"] == name:
                to_delete = house_id
                break

        if to_delete:
            del houses[to_delete]
            data["house"] = houses
            Storage.save(data)
            print("House deleted.")
        else:
            print("House not found or permission denied.")
    
    def do_edit_house(self, arg=None):
        """Edit a house (owners only)"""
        if not self.current_user or self.current_user['role'] != "owner":
            print("Only logged-in owners can edit houses.")
            return

        name = input("House Name: ")
        field = input("Field to edit (name, location, room, price): ")
        new_value = input("New value: ")

        data = Storage.load()
        houses = data.get("house", {})

        for house_id, h in houses.items():
            if h["owner_id"] == self.current_user["id"] and h["name"] == name:
                if field in h:
                    h[field] = float(new_value) if field == "price" else new_value
                    Storage.save(data)
                    print("House updated.")
                    return
                else:
                    print("Invalid field.")
                    return

        print("House not found.")
    
    def do_view_my_houses(self, arg=None):
        if not hasattr(self, 'current_user') or self.current_user["role"] != "owner":
            print("Only logged-in owners can view their houses.")
            return

        data = Storage.load()
        houses = data.get("house", {})

        owner_id = self.current_user["id"]
        owner_houses = [
            house for house in houses.values()
            if house["owner_id"] == owner_id
        ]

        if not owner_houses:
            print("You have not listed any houses yet.")
            return

        print(f"\n🏠 Houses listed by {self.current_user['username']}:\n")
        for i, house in enumerate(owner_houses, start=1):
            print(f"{i}. {house['name']}")
            print(f"   Location: {house['location']}")
            print(f"   Rooms: {house['rooms']}")
            print(f"   Price: ${house['price']}")
            print("-" * 40)

    
    def do_search(self, arg=None):
        """Search houses by location, room count, and price"""
        location = input("Location to search: ")
        min_rooms = int(input("Minimum rooms: "))
        max_price = float(input("Maximum price: "))

        data = Storage.load()
        houses = data.get("house", {})

        matches = [
            h for h in houses.values()
            if h["location"].lower() == location.lower()
            and int(h["rooms"]) >= min_rooms
            and float(h["price"]) <= max_price
        ]

        if not matches:
            print("No houses found.")
        else:
            for h in matches:
                print(f"- {h['name']} | {h['location']} | {h['rooms']} rooms | ${h['price']}")


def do_exit(self, arg):
        """Exit the app"""
        print("Goodbye!")
        return True