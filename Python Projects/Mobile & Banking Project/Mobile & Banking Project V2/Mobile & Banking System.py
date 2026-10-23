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
        self.Bank_Accounts = False
        self.banned = False
        self.creation_date = datetime.now().strftime("%d-%b-%Y %H:%M:%S")

    #Create Random Phone Number
    def phone_generate(self):
        return f"61{random.randint(0, 9999999):07d}"

    @property
    def pin(self):
        return self._pin
    @pin.setter
    def pin(self, new_pin):
        if not isinstance(new_pin, str) or len(new_pin) != 4 or not new_pin.isdigit():
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
            "Bank_Accounts": self.Bank_Accounts,
            "Banned": self.banned,
            "Registeration_Date": self.creation_date,
            "Misc": []
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
class Baccount():

    def __init__(self, bname, lname, bage, bpin):
        self.bname = bname
        self.lname = lname
        self.bage = bage
        self._bpin = bpin
        self._bank_balance = 0.0
        self.account_num = self.bnum_generator()
        self.locked = False
        self.bcreation_date = datetime.now().strftime("%d-%b-%Y %H:%M:%S")

    def bnum_generator(self):
        return f"{random.randint(00000000, 99999999):08d}"

    #Bank PIN View/Change
    @property
    def bpin(self):
        return self._bpin
    @bpin.setter
    def bpin(self, new_bpin):
        if isinstance(new_bpin, str) or len(new_bpin) != 6 and not new_bpin.isdigit():
            print("Invalid Bank PIN, Make Sure the PIN is 6-Digits Long.")
            return
        self._bpin = new_bpin

    #Bank Balance View/Change
    @property
    def bank_balance(self):
        return self._bank_balance
    @bank_balance.setter
    def bank_balance(self, new_bank_balance):
        if isinstance(new_bank_balance, (int,float)) and new_bank_balance < 0:
            print("Invalid Account Balance, It cannot be in Negative.")
            return
        self._bank_balance = new_bank_balance

    def to_bank_dict(self):
        return {
            "First_Name": self.bname,
            "Last_Name": self.lname,
            "Age": self.bage,
            "Account_PIN": self._bpin,
            "Account_Balance": self._bank_balance,
            "Account_Number": self.account_num,
            "Account_Lock": self.locked,
            "Account_Registration_Date": self.bcreation_date
        }

    def verify_bpin(self, bentered):
        return bentered == self._bpin

    def show_binfo(self):
        print(f"First Name: {self.bname}")
        print(f"Last Name: {self.lname}")
        print(f"Age: {self.bage}")
        print(f"Account PIN: {self._bpin}")
        print(f"Account Balance: ${self._bank_balance}")
        print(f"Account Number: {self.account_num}")
        print(f"Account Lock: {self.locked}")
        print(f"Registration_Date: {self.bcreation_date}")

def login():
    print("\n--- Account Login ---")
    username = input("Enter Your Username: ")
    account_info = find_account(username)
    if account_info == None:
        print("Invalid Username")
        return
    entered_pass = input("Enter Your Password: ")
    if account_info["Banned"]:
        print("\nYour Account Is Suspended, Please Contact Support Team.")
        return
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
    account.Bank_Accounts = account_info["Bank_Accounts"]
    account.banned = account_info["Banned"]
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
        print("3. View Your Phone Number")
        print("4. Change Your PIN")
        print("5. Recharge Internet")
        print("6. CBOS Bank")
        print("0. Exit")
        choice = input("Choose a Service: ")
        if choice == "1":
            print(f"Your Current Balance is: ${account.balance:.2f}")
        elif choice == "2":
            local_transfer(account)
        elif choice == "3":
            print(f"Your International Phone Number is: +252{account.phone}")
            print(f"Your Local Phone Number is: 0{account.phone}")
        elif choice == "4":
            change_pin(account)
        elif choice == "5":
            internet_bundle(account)
        elif choice == "6":
            check = load()

            # Find the logged-in user's record
            gb = next(
                (user for user in check
                 if user["Username"] == account.username),
                None
            )

            if gb is None:
                print("Account Was Not Found.")
                continue

            # Create a bank account if the user does not have one
            if not gb["Bank_Accounts"]:
                cbos(account)
                continue

            # Check the logged-in user's bank account lock
            if not gb["Misc"]:
                print("Bank account data was not found.")
                continue

            bank = gb["Misc"][0]
            binfo = Baccount(
                bank["First_Name"],
                bank["Last_Name"],
                bank["Age"],
                bank["Account_PIN"]
            )

            binfo.bank_balance = bank["Account_Balance"]
            binfo.account_num = bank["Account_Number"]
            binfo.locked = bank["Account_Lock"]
            binfo.bcreation_date = bank["Account_Registration_Date"]

            if bank["Account_Lock"]:
                print("\nThe Account is Currently Suspended.")
                print("Please Contact The Bank for more Details.\n")
                continue

            cbos_menu(account, binfo)
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
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN Must Be Exactly 4-Digits ")
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
    pin = input("Enter a 4-Digit PIN: ")
    if pin == "":
        print("PIN, Cannot Be Empty.")
        return
    if len(pin) != 4:
        print("PIN Must Be 4-Digits Long.")
        return
    if not pin.isdigit():
        print("PIN Must Only Containt Digits.")
        return
    if any(char.isalpha() for char in pin) and any(char.isspace() for char in pin):
        print("PIN Can Only Be 4-Digits Long.")
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

def cbos(account):
    name = input("Enter Your First Name: ")
    if name == "":
        print("Name Cannot Be Empty.")
        return
    if any(char.isdigit() for char in name):
        print("Name Cannot Contain Numbers.")
        return
    if name.isspace():
        print("Name Cannot Be Spaces.")
        return
    if name.isdigit():
        print("Name Cannot Be Numbers.")
        return

    laname = input("Enter Your Last Name: ")
    if laname == "":
        print("Name Cannot Be Empty.")
        return
    if any(char.isdigit() for char in laname):
        print("Name Cannot Contain Numbers.")
        return
    if laname.isspace():
        print("Name Cannot Be Spaces.")
        return
    if laname.isdigit():
        print("Name Cannot Be Numbers.")
        return

    age = input("Enter Your Age (xx/xxx/xxxx): ")
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

    bpin = input("Enter a 6-Digit Bank PIN: ")
    if bpin == "":
        print("Bank PIN, Cannot Be Empty.")
        return
    if len(bpin) != 6:
        print("Bank PIN Must Be 4-Digits Long.")
        return
    if not bpin.isdigit():
        print("Bank PIN Must Only Containt Digits.")
        return
    if any(char.isalpha() for char in bpin) and any(char.isspace() for char in bpin):
        print("Bank PIN Can Only Be 6-Digits Long.")
        return

    binfo = Baccount(
        name,
        laname,
        age,
        bpin
    )
    fee = 10
    info = load()
    gb = next((user for user in info if user["Username"] == account.username),None)
    if gb is None:
        print("Account Was Not Found.")
        return
    if gb["Bank_Accounts"]:
        print("You Already Have a Bank Account.")
        return
    if fee > gb["Balance"]:
        print("Insufficient Balance.")
        return

    gb["Bank_Accounts"] = True
    gb["Balance"] -= fee
    account.balance = gb["Balance"]
    account.Bank_Accounts = True
    gb["Misc"].append(binfo.to_bank_dict())
    save(info)

    print(f"\n[CBOS] Thank You For Joining Us Mr.{laname}")
    print(f"Account Opening Fees were: ${fee}")
    print(f"\nYour Current Balance is: ${account.balance}")

def cbos_menu(account, binfo):
    data = load()
    # Find the logged-in user's record
    owner = next(
        (user for user in data
         if user["Username"] == account.username),
        None
    )
    if owner is None:
        print("Account Was Not Found.")
        return
    # Find that user's bank account
    if not owner["Misc"]:
        print("Bank Account Was Not Found.")
        return
    bank = owner["Misc"][0]
    pin = input("Enter Your Bank PIN: ")
    if pin != bank["Account_PIN"]:
        print("Invalid Bank PIN.")
        return
    print(f"\nWelcome Back Mr.{bank['Last_Name']}")
    while True:
        print("==========================")
        print("   Welcome To CBOS Bank")
        print("==========================")
        print("1. View Bank Balance")
        print("2. Transfer Money")
        print("3. Deposit Money From EVCplus Wallet")
        print("4. Withdraw Money To EVCplus Wallet")
        print("5. Change Bank PIN")
        print("0. Exit Menu")
        choice = input("Choose a Service: ")

        if choice == "1":
            if choice == "1":
                print(f"Your Balance is: ${binfo.bank_balance:.2f}")
        elif choice == "2":
            cbos_transfer(account, binfo)
        elif choice == "3":
            pass
        elif choice == "4":
            cbos_withdraw(account, binfo)
        elif choice == "6":
            pass
        elif choice == "0":
            print("Exiting the Menu...")
            time.sleep(1.8)
            break
        else:
            print("Invalid Choice.")

def cbos_transfer(account, binfo):
    data = load()

    owner = next(
        (
            user
            for user in data
            if user["Username"] == account.username), None
    )
    if owner is None or not owner["Misc"]:
        print("Account Was Not Found.")
        return
    sender_bank = owner["Misc"][0]
    pin = input("Enter Your Bank PIN: ")
    if pin != sender_bank["Account_PIN"]:
        print("Incorrect PIN.")
        return
    acc_num = input("Enter The Recipient's Account Number: ")
    if not acc_num.isdigit() or len(acc_num) != 8:
        print("Invalid Account Number. It Must Contain 8 Digits.")
        return
    if acc_num == sender_bank["Account_Number"]:
        print("You Can't Transfer Money To Yourself.")
        return

    # Receivers Account Check
    recipient_bank = None
    for user in data:
        for bank in user["Misc"]:
            if bank["Account_Number"] == acc_num:
                recipient_bank = bank
                break
    if recipient_bank is None:
        print("Recipient Bank Account Was Not Found.")
        return
    if recipient_bank["Account_Lock"]:
        print("The Recipient's Bank Account Is Suspended.")
        return

    try:
        amount = float(input("Enter Amount To Transfer: "))
    except ValueError:
        print("Amount Must Be A Number.")
        return
    if amount <= 0:
        print("Amount Must Be Greater Than Zero.")
        return

    if amount > sender_bank["Account_Balance"]:
        print("Insufficient Bank Balance.")
        return
    print(f"\nRecipient: {recipient_bank['First_Name']} "
          f"{recipient_bank['Last_Name']}")
    print(f"Account Number: {recipient_bank['Account_Number']}")
    print(f"Transfer Amount: ${amount:.2f}")
    confirm = input("Confirm Transfer? (Y/N): ").lower()
    if confirm != "y":
        print("Transfer Cancelled.")
        return

    #Info Saving
    sender_bank["Account_Balance"] -= amount
    binfo.bank_balance = sender_bank["Account_Balance"]
    recipient_bank["Account_Balance"] += amount
    save(data)

    print("\nTransfer Successful!")
    print(f"Amount Transferred: ${amount:.2f}")
    print(
        f"Your Remaining Bank Balance: "
        f"${sender_bank['Account_Balance']:.2f}"
    )

def local_transfer(account):
    data = load()

    own = next(
        (
        user
        for user in data
        if user["Username"] == account.username), None
    )
    if own is None:
        print("Account Was Not Found")
        return
    sender_acc = own
    current_pin = input("Enter Your PIN: ")
    if current_pin != sender_acc["PIN"]:
        print("Incorrect PIN.")
        return
    local_acc = input("Enter Phone Number: ")
    if not local_acc.isdigit() or len(local_acc) != 9 or len(local_acc) > 9:
        print("Invalid Phone Number, Please Use this Format: (61XXXXXXX).")
        return
    if local_acc == sender_acc["Phone_Number"]:
        print("You Can't Transfer Money To Your Self.")
        return

    # Recievers Account Check
    receive = None
    for user in data:
        if user["Phone_Number"] == local_acc:
            receive = user
            break
    if receive is None:
        print("Account Was Not Found.")
        return
    if receive["Banned"]:
        print("Recipient's Account is Suspended, Therefore, You Cannot Transfer Money.")
        return

    try:
        amount = float(input("Enter an Amount: "))
    except ValueError:
        print("Amount Must Be A Number.")
        return
    if amount <= 0:
        print("Amount Must Be Greater Than Zero.")
        return
    if amount > sender_acc["Balance"]:
        print("Insufficient Balance.")
        return

    print(f"\nRecipient's Name: {receive['Name']}")
    print(f"Phone Number: {receive['Phone_Number']}")
    print(f"Amount: ${amount:.2f}")
    ask = input(f"Are You Sure to Transfer ${amount:.2f} to Mr.{receive['Name']} - {receive['Phone_Number']} ?: ").lower()
    if ask != "y":
        print("Transfer Cancelled.")
        return

    sender_acc["Balance"] -= amount
    account.balance = sender_acc["Balance"]
    receive["Balance"] += amount
    save(data)

    print("\nTransfer Successful!")
    print(f"You Have Successfully Transferred ${amount:.2f} to Mr.{receive['Name']} "
          f"with the Phone Number: {receive['Phone_Number']}")
    print(f"Your Current Balance is: ${sender_acc['Balance']:.2f}")

def cbos_withdraw(account, binfo):
    data = load()

    owner = next(
        (
            user
            for user in data
            if user["Username"] == account.username), None
    )

    own = next(
        (
            gold
            for gold in data
            if gold["Username"] == account.username), None
    )
    if owner is None or not owner["Misc"]:
        print("Account Was Not Found.")
        return
    sender = owner["Misc"][0]
    send = own
    pin = input("Enter Your Bank PIN: ")
    if pin != sender["Account_PIN"]:
        print("Incorrect PIN.")
        return

    try:
        amount = float(input("Enter Amount To Transfer: "))
    except ValueError:
        print("Amount Must Be A Number.")
        return
    if amount <= 0:
        print("Amount Must Be Greater Than Zero.")
        return

    if amount > sender["Account_Balance"]:
        print("Insufficient Bank Balance.")
        return

    if sender["Account_Lock"]:
        print("Your Account Is Currently Suspended.")
        return
    ask = input(f"Are you sure to withdraw ${amount:.2f} from Your Bank account {sender['Account_Number']} (Y/N)?: ").lower()
    if ask != "y":
        print("Withdraw Was Cancelled.")
        return

    own["Balance"] += amount
    sender["Account_Balance"] -= amount
    account.balance = own["Balance"]
    binfo.bank_balance = sender["Account_Balance"]
    save(data)

    print(f"${account.balance:.2f}")
    print(f"${binfo.bank_balance:.2f}")

main()
