from utils import dat, save
from datetime import datetime
import random
from card import *
from account import acc_to_acc

def login():
    uname = input("Enter Your Username: ")
    pname = input("Enter Your Password: ")

    for acc in dat["info"]:
        for acc2 in acc["Account_Info"]:
            if uname == acc2["Username"] and pname == acc2["Password"]:
                return acc2

    return None

def ours(account):
    print()
    print("------------------------------------")
    print("What services do you request today?")
    print("------------------------------------")
    print()

    print(
        "1. View account Balance",
        "2. Transfer Money to a local account",
        "3. Transfer Money internationally",
        "4. Change Account pin",
        "5. Transaction History",
        "6. View Account Number",
        "7. Generate a VisaCard",
        "8. View all available Credit Cards",
        sep="\n"
    )

    req = int(input("Choose a number: "))

    if req == 1:
        balance(account)

    elif req == 2:
        ltm(account)

    elif req == 3:
        itm(account)

    elif req == 4:
        change_pin(account)

    elif req == 5:
        Tran_History(account)

    elif req == 6:
        v_acc_num(account)
    elif req == 7:
        CreateVisa(account)
    elif req == 8:
        View_Card(account)
    else:
        print("Invalid number")
def show_balance(account):
    return account["master"][0]["balance"]

def balance(account):
    print(f"Your Balance is: ${show_balance(account)}")

# Local Account to Account Transfer
def ltm(account):

    acc_num = input("Please enter account number: ")

    if not acc_num.isdigit():
        print("Account Number Cannot contain letters or special characters")
        return

    if len(acc_num) <= 7 or len(acc_num) >= 9:
        print("The account number cannot be greater than or lesser than 8 digits")
        return

    receiver = acc_to_acc(acc_num)
    if receiver is None:
        print("Account was not found")
        return

    acc_money = float(input("Enter an amount to transfer: "))

    if acc_money <= 0:
        print("Invalid amount, the value must be greater than 0")
        return

    master = account["master"][0]
    bpin = input("Please enter your pin to verify the transaction: ")

    if bpin != master["pin"]:
        print("Invalid Pin.")
        return

    if acc_money > master["balance"]:
        print("insufficient Balance")
        return

    fee = acc_money * 0.0
    total = acc_money + fee
    master["balance"] = round(master["balance"] - total, 2)

    receiver_master = receiver["master"][0]
    receiver_master["balance"] = round(receiver_master["balance"] + acc_money,2)

    reference = random.randint(0, 99999)
    #Sender Transaction History Saving
    te = {
        "Transaction_Type": "Transfer",
        "Transaction_Direction": "Outgoing",
        "Account_Number": acc_num,
        "Amount_Transferred": acc_money,
        "Date": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
        "Reference_Number": reference,
        "Transferring_Service": "Local",
        "Transfer_Fees": fee
    }
    account["Transaction_History"].append(te)

    #Receiver Transaction History Saving
    tee = {
        "Transaction_Type": "Transfer",
        "Transaction_Direction": "Incoming",
        "Account_Number": master["Account_Number"],
        "Amount_Transferred": acc_money,
        "Date": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
        "Reference_Number": reference,
        "Transferring_Service": "Local",
        "Transfer_Fees": fee
    }
    receiver["Transaction_History"].append(tee)
    save(dat)

    print(
        f"You have successfully transferred ${acc_money:.2f} to {acc_num}",
        f"Transferring fees are: ${fee:.2f}",
        f"Your new Balance is: ${master['balance']:.2f}",
        sep="\n"
    )

# International Account to Account Transfer
def itm(account):

    iacc_num = input("Please enter account number: ")

    if not iacc_num.isdigit():
        print("Account Number Cannot contain letters or special characters")
        return

    if len(iacc_num) <= 11 or len(iacc_num) >= 13:
        print("The account number cannot be greater than or lesser than 12 digits")
        return

    receiver = acc_to_acc(iacc_num)

    if receiver is None:
        print("Account was not found")
        return

    act_money = float(input("Enter an amount to transfer: "))

    if act_money <= 0:
        print("Invalid amount, the value must be greater than 0")
        return

    master = account["master"][0]

    bpin = input("Please enter your pin to verify the transaction: ")

    if bpin != master["pin"]:
        print("Invalid Pin.")
        return

    fee = round(act_money * 0.07, 2)
    total = round(act_money + fee, 2)

    if total > master["balance"]:
        print("insufficient Balance")
        return

    master["balance"] = round(master["balance"] - total, 2)

    receiver_master = receiver["master"][0]
    receiver_master["balance"] = round(receiver_master["balance"] + act_money,2)
    reference = random.randint(0, 99999)

    #Sender Transaction History Saving
    tess = {
        "Transaction_Type": "Transfer",
        "Account_Number": iacc_num,
        "Amount_Transferred": act_money,
        "Date": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
        "Reference_Number": reference,
        "Transferring_Service": "International",
        "Transfer_Fees": fee
    }
    account["Transaction_History"].append(tess)

    # Receiver Transaction History Saving
    tass = {
        "Transaction_Type": "Transfer",
        "Transaction_Direction": "Incoming",
        "Account_Number": master["Com_Account_Number"],
        "Amount_Transferred": act_money,
        "Date": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
        "Reference_Number": reference,
        "Transferring_Service": "International",
        "Transfer_Fees": fee
    }
    receiver["Transaction_History"].append(tass)

    save(dat)
    print(
        f"You have successfully transferred ${act_money:.2f} to {iacc_num}",
        f"Transferring fees are: ${fee:.2f}",
        f"Your new Balance is: ${master['balance']:.2f}",
        sep="\n"
    )

def Tran_History(account):

    master = account["master"][0]

    chek = input("Enter your pin to continue: ")

    if chek != master["pin"]:
        print("Pin is incorrect")
        return

    for number, history in enumerate(account["Transaction_History"],start=1):
        print()
        print(f"Transaction History #{number}")
        print("*" * 24)
        transaction_type = history.get("Transaction_Type")
        if transaction_type == "Transfer" or "Account_Number" in history:
            print(f"Transaction Type: Transfer")
            print(f"Account Number: {history['Account_Number']}")
            print(f"Amount Transferred: ${history['Amount_Transferred']}")
            print(f"Date: {history['Date']}")
            print(f"Reference Number: {history['Reference_Number']}")
            print(f"Transferring Service: {history['Transferring_Service']}")
            print(f"Transfer Fees: ${history['Transfer_Fees']}")
        elif transaction_type == "Card Creation" or "VisaCard_Generating_Fees" in history:
            print(f"Transaction Type: Card Creation")
            print(f"Card Type: {history['Card Type']}")
            print(f"Card Creation Fee: ${history['VisaCard_Generating_Fees']}")
            print(f"Date: {history['Date']}")

def change_pin(account):

    new_bpin = input("Enter your new pin: ")

    if len(new_bpin) <= 5 or len(new_bpin) >= 7:
        print("New pin cannot exceed or be lesser than 6 digits")

    else:

        if not new_bpin.isdigit():
            print("not digit")

        else:

            a_bpin = input("Enter your new pin again: ")

            if new_bpin != a_bpin:
                print("New pin doesnt match the other.")

            else:

                master = account["master"][0]

                master["pin"] = new_bpin

                save(dat)

                print("Pin was changed successfully")

def v_acc_num(account):

    master = account["master"][0]

    veriPin = input("Enter Your pin: ")

    if veriPin != master["pin"]:
        print("Incorrect pin")

    else:
        print(f"Account Number (Local): {master['Account_Number']}")
        print(f"Account Number (International): {master['Com_Account_Number']}")

