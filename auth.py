import art
import main
from getpass import getpass
import database
import pwinput


def register():
    global username
    global email
    global password
    
    print(art.register)
    username = input("username:\n")
    email = input("email:\n")
    password = pwinput.pwinput("password:\n")
    ver_password = pwinput.pwinput("verify password:")
    if password == ver_password:
        print(main.bcolors.OKGREEN + "Registration successful!" + main.bcolors.ENDC)
        database.succ_registration()
    else:
        print(main.bcolors.RED + "Registration failed - Password doesn't match!" + main.bcolors.ENDC)
        register()
def login():
    print(art.login)
    user = input("username:\n")
    password = pwinput.pwinput("password:\n")
    if user and password in database.result:
        print(main.bcolors.OKGREEN + "Login Successful!" + main.bcolors.ENDC)