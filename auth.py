import art
import main
from getpass import getpass
import database


def register():
    global username
    global email
    global password
    
    print(art.register)
    username = input("username:\n")
    email = input("email:\n")
    password = input("password:\n")
    ver_password = input("verify password:")
    if password == ver_password:
        print(main.bcolors.OKGREEN + "Registration successful!" + main.bcolors.ENDC)
        database.succ_registration()
    else:
        print(main.bcolors.RED + "Registration failed" + main.bcolors.ENDC)
def login():
    print(art.login)
    user = input("username:\n")
    password = input("password:\n")