from storage import Storage
from functions import AirbnbApp
import os
import json

def ensure_storage_file():
    """Create the storage JSON file if it doesn't exist."""
    if not os.path.exists(Storage.FILE):
        with open(Storage.FILE, "w") as f:
            json.dump({"users": {}, "house": {}}, f, indent=4)

def main():
    ensure_storage_file()
    print("Welcome to the Airbnb Terminal!\n")
    app = AirbnbApp()

    # Force login or registration before anything else
    while not getattr(app, 'current_user', None):
        auth = input("Do you want to [register], [login], or [quit]? ").strip().lower()

        if auth == "register":
            app.do_register()
            app.do_login()
        elif auth == "login":
            app.do_login()
        elif auth == "quit":
            print("Goodbye!")
            return
        else:
            print("Invalid input. Please enter 'register', 'login', or 'quit'.")

    # Main command loop
    while True:
        command = input(
            "\nWhat would you like to do?\n"
            "[add house / edit house / delete house / search / view my houses / logout]: "
        ).strip().lower()

        if command == "add house":
            app.do_add_house()
        elif command == "edit house":
            app.do_edit_house()
        elif command == "delete house":
            app.do_delete_house()
        elif command == "search":
            app.do_search()
        elif command == "view my houses":
            app.do_view_my_houses()
        elif command == "logout":
            print("Logging out. Goodbye!")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
