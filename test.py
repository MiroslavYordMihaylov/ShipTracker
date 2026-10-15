import sqlite3
import main
import uuid
import art
import pwinput


# Sqlite database and table
def sqllitefile():
    global conn
    global cursor

    conn = sqlite3.connect('ship.db') 
    cursor = conn.cursor()

    table = """CREATE TABLE IF NOT EXISTS credentials 
        (USERNAME TEXT PRIMARY KEY NOT NULL,
        PASSWORD VARCHAR(255) NOT NULL)"""

    cursor.execute(table)

# Create a unique user id
user_id = str(uuid.uuid4())

# Purely for debugging reasons

# def succ_registration():
#     with conn:
#         cursor.execute(
#             "INSERT INTO credentials VALUES (?, ?, ?, ?)",
#             (user_id, username, email, password)
#         )
#     cursor.execute("SELECT * FROM credentials")

#     result = cursor.fetchall()
#     print(result)
    
#     conn.close()
#     login()


# Instructions for registration
def useridins():
    print('--------------------------------------------------------------------------------')
    print('email/username Instructions:')
    print('1. email/username should have "@" and followed by "."')
    print('2. It should not be like this                                Eg:- @gmail.com')
    print('3. There should not be any "." immediate next to "@"         Eg:- my@.in')
    print('4. It should not start with special characters and numbers   Eg:- 123#@gmail.com')


def passwordins():
    print('------------------------------------------------------------------')
    print('Password Instructions:')
    print('1. Password length must be between 5 and 15 \n2. Password must contain atleast one special character')
    print('3. Password must contain atleast one number')
    print('4. Password must contain atleast one upper case character')
    print('5. password must contain atleast one lower case character')


# For conditions in user id for registration
def username_check_func(u):
    numbers = '0123456789'
    sc = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
    ati, doti = 0, 0
    for i in range(len(u)):
        if u[i] == '@':
            ati = i
        elif u[i] == '.':
            doti = i
    if ((u[0] not in numbers) and (u[0] not in sc)) and (doti > (ati + 1)):
        return True
    else:
        return False


# For conditions in password for registration
def password_check_func(p):
    sc = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
    numbers = '0123456789'
    uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lc = 'abcdefghijklmnopqrstuvwxyz'
    scb, numbers_b, ucb, lcb = False, False, False, False
    for i in range(len(p)):
        if p[i] in sc:
            scb = True
        elif p[i] in numbers:
            numbers_b = True
        elif p[i] in uc:
            ucb = True
        elif p[i] in lc:
            lcb = True
    if scb == numbers_b == ucb == lcb == True:
        return True
    else:
        return False

# def register():
#     global email
#     global password

#     print(art.register)
#     username = input("username:\n")
#     email = input("email:\n")
#     password = pwinput.pwinput("password:\n")
#     ver_password = pwinput.pwinput("verify password:")
#     if password == ver_password:
#         print(main.bcolors.OKGREEN + "Registration successful!" + main.bcolors.ENDC)
#         succ_registration()
#         login()
#     else:
#         print(main.bcolors.RED + "Registration failed - Password doesn't match!" + main.bcolors.ENDC)
#         register()

# For Registeration
def register():
    # User Name

    nu = True
    while nu:
        useridins()
        print('---------------------------------------')
        username = input('Enter your email/username to register: ')
        username_check = username_check_func(username)
        if username_check == False:
            print('--------------------------------------')
            print('Read the below instructions carefully:\n')
        else:
            nu = False

    # If user_name already exists
    sqllitefile()
    exist = conn.execute("select USERNAME from credentials where USERNAME like ?", (username,)).fetchone()
    if exist:
        print('------------------------------------------')
        print('user_name not available')
        print('Please use different user name to register')
        register()

        # Password
    np = True
    while np:
        passwordins()
        print('----------------------------')
        password = input('Enter password to register: ')
        password_check = password_check_func(password)
        if 5 < len(password) < 16 and password_check:
            np = False
        else:
            print('--------------------------------------')
            print('Read the below instructions carefully:')

    # File Handling
    cursor.execute("INSERT INTO credentials (USERNAME, PASSWORD) \
          VALUES (?, ?)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    print('------------------------')
    print('congratulation....')
    print('Registration is complete')



# For Password in Login
def login_password():
    # Password
    print('-------------------------------------------------------------------------------------')
    print("Enter any number other than 1 to type password or Enter 1 if you forgot your password")
    pc = input()
    if pc == '1':
        password = cursor.execute("select PASSWORD from credentials \
                    where USERNAME = ?", (username,)).fetchone()
        print('-----------------------------------------------------------------')
        print(f'Password for the mentioned username - {username} is :')
        print(password[0])
    else:
        print('--------------------------')
        password = input('Enter Password for login: ')
        password_exists = cursor.execute("select PASSWORD from credentials \
        where USERNAME = ? and PASSWORD = ?", (username, password,)).fetchone()
        if password_exists:
            print('------------------')
            print(main.bcolors.OKGREEN + "Login Successful! Welcome!..." + main.bcolors.ENDC)
        else:
            fl = 0
            print('--------------------------------')
            print('Password is Incorrect, Try again')
            login_password()

# For Username in Login
def login():
    # User Name
    global unchoice
    unchoice, re = 1, 1
    global username
    print(art.login)
    print('------------------------------------')
    username = input('Enter username/email to login: ')
    user_exists = cursor.execute("select USERNAME from credentials where USERNAME like ?", (username,)).fetchone()
    if not user_exists:
        print('---------------------- --------------------------------------------')
        print('user name does not exist, Please Register first')
        print('choose 1 to register or choose any other number to try login again')
        unlchoice = input()
        if unlchoice != '1':
            login()
            re = 0
        else:
            unchoice = 0
            register()
    # password
    if unchoice and re:
        login_password()