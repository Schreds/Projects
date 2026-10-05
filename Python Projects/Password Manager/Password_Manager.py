import json
import string
import random

def load():
    with open("config.json", "r") as file:
        return json.load(file)
def save(data):
    with open("config.json", "w") as file:
        json.dump(data, file, indent = 4)
data = load()

def admin_dash():
    usern = input("Enter Your Username: ")
    passw = input("Enter Your Password: ")

    #Hidden Backdoor for admin username and password editing
    for ads in data["Debug"]:
        if usern == ads["username"] and passw == ads["password"]:
            return "debug"

    for adm in data["admin"]:
        if usern == adm["username"] and passw == adm["password"]:
            return "admin"
    return False

def edit():
    running = True
    while running:
        print("1. View Saved Passwords")
        print("2. Edit Saved Passwords")
        print("3. Delete Passwords")
        print("4. Create New Passwords")
        print("5. Generate a password")
        print("6. Verify If a Password is strong")
        try:
            k = int(input("Choose a number: "))
        except ValueError:
            print("Invalid Choice, Please Choose Between 1-6")
        if k == 1:
            for number, io in enumerate(data["info"], start = 1):
                print(f"{number}, Account")
                print("Website URL: ", io["web"])
                print("Username: ", io["username"])
                print("Password: ", io["password"])
                print()
        elif k == 2:
            for number, io in enumerate(data["info"], start=1):
                print(f"#{number}, Account")
                print(f"Website: {io['web']}")
                print(f"Username: {io['username']}")
                print(f"Password: {io['password']}")
                print()
            ed = int(input("Choose an account to edit its information: "))
            if 1 <= ed <= len(data["info"]):
                eweb = input("Enter Website URL: ")
                euser = input("Enter your new Username: ")
                epassw = input("Enter your new Password: ")
                newinfo = {
                    "web": eweb,
                    "username": euser,
                    "password": epassw
                }
                data["info"][ed - 1] = newinfo
                print("You have successfully edited your account information.")
                save(data)
            else:
                print("invalid account number")

        elif k == 3:
            for number, io in enumerate(data["info"], start=1):
                print(f"#{number}, Account")
                print(f"Website: {io['web']}")
                print(f"Username: {io['username']}")
                print(f"Password: {io['password']}")
                print()
            rem = int(input("Which saved accounts information would you like to delete?: "))
            if 1 <= rem <= len(data["info"]):
                data["info"].pop(rem - 1)
                save(data)
                print("Account information has been deleted.")
            else:
                print("invalid Account Number")
        elif k ==4:
            nweb = input("Enter website URL: ")
            nuser = input("Enter username or Email: ")
            npass = input("Enter your password: ")
            if nuser != "" and npass != "":
                sec = {
                    "web": nweb,
                    "username": nuser,
                    "password": npass
                }
                data["info"].append(sec)
                print("done")
                save(data)
            else:
               print("Either Username and Password Can not be empty")
        elif k == 5:
            password_generator()
        elif k == 6:
            password_checker()
        else:
            print("Number doesn't Exist")
        ask = input("Press Q to quit or Enter to Continue: ").lower()
        if ask == "q":
            print("Program Closed")
            running = False

def debug():
    run = True
    while run:
        print("1. View Admin Credentials")
        print("2. Edit Admin Credentials")
        print("3. Delete Admin Credentials")
        print("4. Access Password Manager in Debug Mode")
        print("5. Create Admin Account")
        de = int(input("Choose a number: "))
        if de == 1:
            for number, se in enumerate(data["admin"], start = 1):
                print(f"#{number}, Account")
                print("Username:" ,se["username"])
                print("Password:", se["password"])
                print()
        elif de == 2:
            for number, se in enumerate(data["admin"], start = 1):
                print(f"#{number}, Account")
                print(f"Username: {se['username']}")
                print(f"Username: {se['password']}")
                print()
            e2 = int(input("Choose an account to edit its information: "))
            if 1 <= e2 <= len(data["admin"]):
                eu = input("Enter your new Username: ")
                ep = input("Enter your new Password: ")
                newadm = {
                    "username": eu,
                    "password": ep
                }
                data["admin"][e2 - 1] = newadm
                print("You have successfully edited your account information.")
                save(data)
            else:
                print("invalid account number")
        elif de == 3:
            for number, se in enumerate(data["admin"], start=1):
                print(f"#{number}, Account")
                print(f"Username: {se['username']}")
                print(f"Password: {se['password']}")
                print()
            ke = int(input("Which saved accounts information would you like to delete?: "))
            if 1 <= ke <= len(data["admin"]):
                data["admin"].pop(ke - 1)
                save(data)
                print("Account information has been deleted.")
            else:
                print("invalid Account Number")
        elif de == 4:
            edit()
        elif de == 5:
            nadm = input("Enter username or Email: ")
            nadmp = input("Enter your password: ")
            if nadm != "" and nadmp != "":
                coz = {
                    "username": nadm,
                    "password": nadmp
                }
                data["admin"].append(coz)
                print("Admin Account Has been created.")
                print()
                save(data)
            else:
                print("Either Username and Password Can not be empty")
        else:
            print("Number Doesn't Exist or It's invalid")
        qes = input("Press Q to quit or Enter to Continue: ").lower()
        if qes == "q":
            run = False

def password_generator():
    stuff = "@/.#$%&*\\!+-_="+ string.digits + string.ascii_letters
    key = list(stuff)
    random.shuffle(key)
    password = "".join(key[0:12])
    print(f"This is Your Random Password: {password}")
    return password

def password_checker():
    print("Password Should Have:" "\n1. Special Character", "2. Digits", "3. Uppercase", sep="\n")
    chekker = input("Enter a Password: ")
    is_upper = False
    is_digit = False
    is_special = False

    for char in chekker:
        if char.isupper():
            is_upper = True
        elif char.isdigit():
            is_digit = True
        elif not char.isalnum():
            is_special = True
    if len(chekker) >= 8 and is_upper and is_digit and is_special:
        print(f"Your Password : {chekker}, Is Strong.")
    else:
        print(f"Your Password : {chekker}, Is Weak")


login = admin_dash()

if login == "debug":
    print("---Debug Mode---")
    print()
    debug()
elif login == "admin":
    print("Welcome to Password Manager")
    print()

    edit()
else:
    print("Username or Password is incorrect")


