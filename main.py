import art
import os
import auth


yes = ["y", "yes", "", " "]
no = ["n", "no"]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[0;31m'

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
            auth.login()
        elif answer in no:
            auth.register()
        else:
            print("Please respond with 'yes' or 'no'")
            main_menu()
            
def open_websocket():
    pass

if __name__ == "__main__":
    main()