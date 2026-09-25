import random
from utils import *
from datetime import datetime
def MasterCard():
    CardN = "52" + f"{random.randint(0, 99999999999999):014d}"
    Cexp = f"{random.randint(1,12):02d}/{random.randint(28, 37)}"
    CVV = f"{random.randint(1,999):03}"
    Card_Type = "Debit Mastercard"
    return CardN, Cexp, CVV, Card_Type

def VisaCard():
    CardN = "42" + f"{random.randint(0,99999999999999):014d}"
    Cexp = f"{random.randint(1,12):02d}/{random.randint(28,37)}"
    CVV = f"{random.randint(1,999):03}"
    Card_Type = "Visa"
    return CardN, Cexp, CVV, Card_Type

def CreateVisa(account):
    CardN, Cexp, CVV, Card_Type = VisaCard()
    master = account["master"][0]
    holder_name = account["Name"]
    visa = {
        "Card_Type": Card_Type,
        "Card_Number": CardN,
        "Expiring_Date": Cexp,
        "CVV": CVV,
        "Card_Holder_Name": holder_name,
        "Credit_Limit": 5000,
        "Used_Credit": 0,
        "Debt": 0,
        "Interest_Rate": 0.10,
        "Credit_Limit_Lock": False,
        "Credit_Block": True
    }
    pver = input("Enter your pin to verify: ")

    if pver != master["pin"]:
        print("Invalid pin")
    else:
        creation_fee = round(35.75, 2)
        if creation_fee > master["balance"]:
            print("Insufficient Balance")
        else:
            master["balance"] -= creation_fee
            master["balance"] = round(master["balance"], 2)
            master["Cards"].append(visa)
            fee_card = {
                "Transaction_Type": "Card Creation",
                "Card Type": "Visa",
                "VisaCard_Generating_Fees": creation_fee,
                "Date": datetime.now().strftime("%d-%b-%Y %H:%M:%S")
            }
            account["Transaction_History"].append(fee_card)
            save(dat)
            print("*" * 29)
            print("VisaCard was created successfully")
            print("*" * 29)
            print(f"Card Type: {Card_Type}")
            print(f"Card Number: {CardN}")
            print(f"Expiry: {Cexp}")
            print(f"CVV: {CVV}")
            print(f"Card Holder's Name: {holder_name}")
            print()
            print(f"Card Fee: {creation_fee}")
            print(f"Your account balance is: ${master['balance']:.2f}")

def View_Card(account):
    cards = account["master"][0]["Cards"]
    holder_name = account["Name"]
    if len(cards) == 0:
        print("You have no cards.")
        return
    print(f"You have {len(cards)} card(s).")

    for number, card in enumerate(cards, start=1):
        print()
        print(f"Card #{number}")
        print(f"Type: {card['Card_Type']}")
        print(f"Number: {card['Card_Number']}")
        print(f"Expiry: {card['Expiring_Date']}")
        print(f"CVV: {card['CVV']}")
        print(f"Card Holder's Name: {holder_name}")
        if card["Card_Type"] == "Debit Mastercard":
            if card["Credit_Block"] == True:
                print(f"Card Status: Blocked")
            else:
                print("Card Status: Unlocked")
        if card["Card_Type"] == "Visa":
            print(f"Available Loan: ${card['Credit_Limit']:.2f}")
            if card["Credit_Block"] == True:
                print(f"Card Status: Blocked")
            else:
                print("Card Status: Unlocked")

"""
1. Card blocked cannot be used
2. Card loan available to be used
"""