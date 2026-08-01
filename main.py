import art
from getpass import getpass
import subprocess
import os
import websockets
import websocket
yes = ["y", "yes", "", " "]
no = ["n", "no"]

def main():
    print(art.caption)
    input("\n[Press enter to continue]")

    entry_responce = input("Would you like to go offline? (None of the data will be saved) Y/n\n").lower()
    if entry_responce in yes:

        print("Searching for ships!..")
        os.startfile("websocket.py")
        close = input()
        if close == "stop":
            pass
        else:
            pass
    elif entry_responce in no:
        main_menu()
    else:
        print("Please respond with 'yes' or 'no'")
        main_menu()

def main_menu():
    # print(art.ship)
        answer = input("Do you have an account? Y/n?\n").lower()
        
        if answer in yes:
            login()
        elif answer in no:
            register()
        else:
            print("Please respond with 'yes' or 'no'")
            main_menu()
            

def register():
    print(art.register)

def login():
    print(art.login)
    user = input("username: ")
    password = input("password: ")

def open_websocket():
    pass

if __name__ == "__main__":
    main()