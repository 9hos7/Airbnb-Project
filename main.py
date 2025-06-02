from user import User
from house import House
from storage import Storage
from functions import AirbnbApp

user = User
house = House
storage = Storage
do = AirbnbApp

print("Welcome to the Airbnb Terminal!")
auth = input("Register or Login: ").lower

if auth == "register":
    do.do_register
    do.do_login
elif auth == "login":
    do.do_login

in_use = True

while in_use:
    to_do = input("What would you like to do today? ").lower

    if to_do == "add_house":
        do.add_house
    elif to_do == "edit_house":
        do.edit_house
    elif to_do == "delete_house":
        do.delete_house
    elif to_do == "search":
        do.search
    else:
        print("Invalid Command")