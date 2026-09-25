from utils import dat, save
from datetime import datetime
import random
from card import MasterCard, VisaCard

def generate_account_numbers():

    # Generate 8 digit local account number
    local = f"{random.randint(0, 99999999):08d}"

    # Generate 4 extra digits
    extra = f"{random.randint(0, 9999):04d}"

    # International account starts with the exact local account number
    international = local + extra

    return local, international

def create():

    print("*" * 33)
    print("Glad to see you joining CBS Bank")

    nuname = input("Enter your full name: ")

    if nuname == "":
        print("Full name cannot be empty.")
        return

    nuemail = input("Enter your Email Address: ")

    if nuemail == "":
        print("Email Address cannot be empty.")
        return

    nuphone = input("Enter your phone number: ")

    if nuphone == "":
        print("Phone Number cannot be empty.")
        return

    nudob = input("Enter your birthday: ")

    if nudob == "":
        print("Date of birth cannot be empty.")
        return

    if len(nudob) <= 9 or len(nudob) >= 12:
        print("Please make sure to use either (xx/xx/xxxx) or (xx/jan/xxxx).")
        return

    nupob = input("Enter your place of birth: ")

    if nupob == "":
        print("Place of Birth cannot be empty.")
        return

    nuaddress = input("Enter your address: ")

    if nuaddress == "":
        print("Address cannot be empty.")
        return

    nUsername = input("Enter your Username: ")

    if nUsername == "":
        print("Username Cannot be empty")
        return

    if len(nUsername) <= 3 or len(nUsername) >= 17:
        print("Username cannot be lesser than 4 character or greater than 16 characters")
        return

    nuPassword = input("Enter your Password: ")

    if nuPassword == "":
        print("Password Cannot be empty.")
        return

    if len(nuPassword) <= 7 or len(nuPassword) >= 19:
        print("Password must be between 8 to 18 characters long")
        return

    nuPin = input("Enter a 6 digit pin: ")

    if nuPin == "":
        print("Pin cannot be empty.")
        return

    if len(nuPin) <= 5 or len(nuPin) >= 7:
        print("Pin number must be 6 digits")
        return

    if not nuPin.isdigit():
        print("Pin must contain numbers only.")
        return

    # Generate Local + International account numbers
    lan, ian = generate_account_numbers()

    CardN, Cexp, CVV,Card_Type = MasterCard()


    acc_info = {

        "Name": nuname,

        "Email Address": nuemail,

        "Phone Number": nuphone,

        "DOB": nudob,

        "POB": nupob,

        "Address": nuaddress,

        "Username": nUsername,

        "Password": nuPassword,

        "Registration Date":
            datetime.now().strftime("%d-%b-%Y %H:%M:%S"),

        "master": [
            {
                "Account_Number": lan,

                "Com_Account_Number": ian,

                "balance": 0,

                "pin": nuPin,

                "Cards": [{
                    "Card_Type": Card_Type,
                    "Card_Number": CardN,
                    "Expiring_Date": Cexp,
                    "CVV": CVV,
                    "Card_Holder_Name":nuname,
                    "Credit_Limit_Lock": False,
                    "Credit_Block": True

                }]
            }
        ],

        "Transaction_History": []
    }

    dat["info"][0]["Account_Info"].append(acc_info)

    save(dat)

    print(
        "Account was created Successfully.",
        "Thank you for Choosing CBS Bank",
        sep="\n"
    )

def acc_to_acc(key):
    for group in dat["info"]:
        for user_account in group["Account_Info"]:
            master = user_account["master"][0]
            if key == master["Account_Number"] or key == master["Com_Account_Number"]:
                return user_account
    return None


