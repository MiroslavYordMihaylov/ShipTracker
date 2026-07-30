import art
from getpass import getpass

def main():
    print(art.caption)
    input("\n[Press enter to continue]")

    main_menu()

def main_menu():
    yes = ["y", "yes", "", " "]
    no = ["n", "n"]
    # print(art.ship)
    
    answer = input("Do you have an account? Y/n?\n").lower()
    
    if answer in yes:
        login()
    elif answer in no:
        register()
    else:
        print("Please respond with 'yes' or 'no'")

def register():
    print(art.register)

def login():
    print(art.login)

if __name__ == "__main__":
    main()