from storage import Storage
from functions import AirbnbApp

storage = Storage()
do = AirbnbApp()

print("Welcome to the Airbnb Terminal!")
auth = input("Register or Login: ").lower

if auth == "register":
    do.do_register()
    do.do_login()
elif auth == "login":
    do.do_login()

in_use = True

while in_use:
    to_do = input("What would you like to do today? ").lower

    if to_do == "add house":
        do.do_add_house()
    elif to_do == "edit house":
        do.do_edit_house()
    elif to_do == "delete house":
        do.do_delete_house()
    elif to_do == "search":
        do.do_search()
    else:
        print("Invalid Command")
