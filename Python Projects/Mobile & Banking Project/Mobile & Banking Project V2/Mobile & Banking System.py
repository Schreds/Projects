import random
import json
import time
from datetime import datetime
FILE = "test.json"
def load():
    with open(FILE, "r") as file:
        return json.load(file)
def save(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent = 4)
def find_account(username):
    accounts = load()
    for account in accounts:
        if account["Username"] == username:
            return account
    return None

class Account():

    def __init__(self, name, age, username, password, pin, phone):
        self.name = name
        self.age = age
        self.username = username
        self.password = password
        self._pin = pin
        self.phone = self.phone_generate()
        self._balance = 0.0
        self.creation_date = datetime.now().strftime("%d-%b-%Y %H:%M:%S")

    #Create Random Phone Number
    def phone_generate(self):
        return f"61{random.randint(0, 9999999):07d}"

    @property
    def pin(self):
        return self._pin
    @pin.setter
    def pin(self, new_pin):
        if not isinstance(new_pin, str) or len(new_pin) != 6 or not new_pin.isdigit():
            print("Invalid PIN. Please enter exactly 6 digits.")
            return
        self._pin = new_pin

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, new_balance):
        if isinstance(new_balance, (int,float)) and new_balance < 0:
            print("Balance Cannot Be Negative.")
            return
        self._balance = new_balance

    def to_dict(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Username": self.username,
            "Password": self.password,
            "PIN": self._pin,
            "Phone_Number": self.phone,
            "Balance": self.balance,
            "Registeration_Date": self.creation_date
        }

    def verify_password(self, entered_pass):
        return entered_pass == self.password

    def veri_pin(self, current_pin):
        return current_pin == self.pin

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print(f"PIN: {self._pin}")
        print(f"Phone Number: {self.phone}")

def login():
    print("\n--- Account Login ---")
    username = input("Enter Your Username: ")
    account_info = find_account(username)
    if account_info == None:
        print("Invalid Username")
        return
    entered_pass = input("Enter Your Password: ")
    account = Account(
        account_info["Name"],
        account_info["Age"],
        account_info["Username"],
        account_info["Password"],
        account_info["PIN"],
        account_info["Phone_Number"]
    )
    account.phone = account_info["Phone_Number"]
    account.balance = account_info["Balance"]
    account.name = account_info["Name"]
    if not account.verify_password(entered_pass):
        print("Invalid Password")
        return
    print(f"\nWelcome Back, {account.username}")

    return account

def account_menu(account):
    while True:
        print("\n==========================")
        print("       ACCOUNT MENU")
        print("==========================")

        print("1. View Balance")
        print("2. Transfer Money Locally")
        print("3. Transfer Money Internationally")
        print("4. View Your Phone Number")
        print("5. Change Your PIN")
        print("6. Recharge Internet")
        print("0. Exit")
        choice = input("Choose a Service: ")
        if choice == "1":
            print(f"Your Current Balance is: ${account.balance:.2f}")
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            print(f"Your International Phone Number is: +252{account.phone}")
            print(f"Your Local Phone Number is: 0{account.phone}")
        elif choice == "5":
            change_pin(account)
        elif choice == "6":
            internet_bundle(account)
        elif choice == "0":
            print("Loggin Out...")
            time.sleep(1.5)
            print(f"\nWe're Glad You've Used EVCplus Mobile App Service Mr,{account.username}")
            break
        else:
            print("Invalid Choice")

def change_pin(account):
    current_pin = input("Enter Your Current PIN: ")
    if not account.veri_pin(current_pin):
        print("Incorrect PIN.")
        return
    new_pin = input("Enter Your New PIN: ")
    if len(new_pin) != 6 or not new_pin.isdigit():
        print("PIN Must Be Exactly 6-Digits ")
        return
    if new_pin == current_pin:
        print("\nYou Can't set your old PIN as your New PIN.")
        return
    confirm_pin = input("Confirm Your New PIN: ")
    if new_pin != confirm_pin:
        print("PINs Do not Match.")
        return
    account.pin = new_pin
    accounts = load()
    for acc in accounts:
        if acc["Username"] == account.username:
            acc["PIN"] = account.pin
            break
    save(accounts)
    print("PIN Changed Successfully!")

def cra():
    name = input("Enter Your Full Name: ")
    if name == "":
        print("Name Cannot Be Empty.")
        return
    if any(char.isdigit() for char in name) :
        print("Name Cannot Contain Numbers")
        return
    if name.isdigit():
        print("Name Cannot Be Digits.")
        return
    age = input("Enter Your age (xx/xxx/xxxx): ")
    if age == "":
        print("Age Cannot Be Empty.")
        return
    if age.isspace():
        print("Age Cannot Contain Spaces.")
        return
    if any(char.isspace() for char in age):
        print("Age Cannot Contain Spaces.")
        return
    if len(age) < 11:
        print("Invalid Age, Please Use This Format (xx/xxx/xxxx)")
        return
    username = input("Enter Your Username: ")
    if username == "":
        print("Username Cannot Be Empty.")
        return
    if len(username) < 4:
        print("Username Is too short.")
        return
    if username.isspace():
        print("Username Cannot Be Spaces.")
        return
    if find_account(username) is not None:
        print("Username Is Already Taken")
        return
    password = input("Enter Your Password: ")
    if password == "":
        print("Password Cannot Be Empty.")
        return
    if len(password) < 8:
        print("Invalid Password, Password Must be longer than 8 Character Or Digits.")
        return
    if password.isspace():
        print("Password Cannot Be Spaces.")
        return
    if any(char.isspace() for char in password):
        print("Password Cannot Containt Spaces.")
        return
    pin = input("Enter a 6-Digit PIN: ")
    if pin == "":
        print("PIN, Cannot Be Empty.")
        return
    if len(pin) != 6:
        print("PIN Must Be 6-Digits Long.")
        return
    if not pin.isdigit():
        print("PIN Must Only Containt Digits.")
        return
    if any(char.isalpha() for char in pin) and any(char.isspace() for char in pin):
        print("PIN Can Only Be 6-Digits Long.")
        return

    acc = Account(
        name,
        age,
        username,
        password,
        pin,
        None
    )
    accounts = load()
    accounts.append(acc.to_dict())
    save(accounts)
    print(f"\n{acc.name}, Your Account was Created Successfully.")
    print(f"Your Phone Number is: '0{acc.phone}'")

def main():
    while True:
        print("Welcome EVCplus Mobile App")
        print("1. Login")
        print("2. Create an Account")
        print("0. Exit")
        choice = input("Choose a Service: ")
        if choice == "1":
            success_account = login()
            if success_account is not None:
                account_menu(success_account)

        elif choice == "2":
            cra()
        elif choice == "0":
            print("Shutting Down All Services...")
            time.sleep(1.8)
            print("\nSystem Closed.")
            break
        else:
            print("\nInvalid Choice")

def internet_bundle(account):
    packages = {
        "1": ("24 Hours", 1.00),
        "2": ("12 Hours", 0.35),
        "3": ("6 Hours", 0.20),
        "4": ("3 Hours", 0.15),
        "5": ("30 Days", 18.5)
    }
    while True:
        print("1. Unlimited Internet for 24 Hours $1")
        print("2. Unlimited Internet for 12 Hours $0.35")
        print("3. Unlimited Internet for 6 Hours $0.20")
        print("4. Unlimited Internet for 3 Hours $0.15")
        print("5. Unlimited Internet for 30 Days $18.5")
        print("0. Exit This Menu")

        choice = input("Choose a Service: ")
        if choice == "0":
            print("Exiting Internet Bundle Service.")
            break
        if choice not in packages:
            print("Invalid Choice.")
            continue
        duration, price = packages[choice]
        print(f"\nSelected Package: {duration} Unlimited Internet")
        print(f"Package Price: ${price:.2f}")
        print(f"Your Current Balance: ${account.balance:.2f}")

        if price > account.balance:
            print("Insufficient Balance.")
            continue
        ask = input(f"Confirm Purchase for ${price:.2f}? (Y/N): ").lower()
        if ask == "n":
            print("Purchae Canncelled.")
            continue
        if ask != "y":
            print("Invalid Answer.")
            continue
        accounts = load()
        for acc in accounts:
            if acc["Username"] == account.username:
                if price > acc["Balance"]:
                    print("Insufficient Balance.")
                    return
                acc["Balance"] -= price
                account.balance = acc["Balance"]
                save(accounts)

                print("\nInternet Bundle Purchased Successfully!")
                print(f"Package Duration: {duration} Unlimited Internet")
                print(f"Amount Paid: ${price:.2f}")
                print(f"Remaining Balance: ${account.balance:.2f}")
                break
            else:
                print("Account Was Not Found.")

main()

