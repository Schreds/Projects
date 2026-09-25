#EVCplus Project in Python

import time
import random
import json



with open("info.json", "r") as EVC:
    sim = json.load(EVC)

running = True

while running:

    user = int(input("Please enter a pin: "))
    print("-" * 50)
    if user != sim["pin"]:
        print("The pin is wrong")
    elif user == sim["pin"]:
        dic = ["1. Show me my balance", "2. Recharge Phone calls", "3. Recharge Internet", "4. Send Money", "5. Salaam Bank", "6. Change Pin"]
        for x in dic:
            print(x)
        userr = int(input("Please Choose a number: "))

        #Show balance

        if userr == 1:
            print(f"Your balance is: {sim["balance"]:.2f}$ ")
        elif userr == 2:
            print()
            dic2 = ["1. Recharge local Airtime", "2. Recharge International Airtime"]
            for y in dic2:
                print(y)
            rech = int(input("Please Choose a number: "))

            #Airtime Recharge

            if rech == 1:
                sdec = ["1. 1$ for 80 Minutes", "2. 5$ for 400 Minutes", "3. 10$ for 800 Minutes", "4. 20$ for 1600 Minutes"]
                for z in sdec:
                    print(z)
                rech1 = int(input("Please Choose a number: "))
                if rech1 == 1:
                    ye = input("Are you sure you want to pay 1$ for 80 Minutes? (Yes or No): ").lower()
                    if ye == "yes":
                        print("You have successfully recharged", "It will expire after 30 days", sep="\n")
                    else:
                        print("You have successfully canceled ordering")
                elif rech1 == 2:
                    ya = input("Are you sure you want to pay 5$ for 400 Minutes? (Yes or No): ").lower()
                    if ya == "yes":
                        print("You have successfully recharged", "It will expire after 30 days", sep="\n")
                    else:
                        print("You have successfully canceled ordering")
                elif rech1 == 3:
                    yea = input("Are you sure you want to pay 10$ for 800 Minutes? (Yes or No): ").lower()
                    if yea == "yes":
                        print("You have successfully recharged", "It will expire after 70 days", sep="\n")
                    else:
                        print("You have successfully canceled ordering")
                elif rech1 == 4:
                    yea1 = input("Are you sure you want to pay 20$ for 1600 Minutes? (Yes or No): ").lower()
                    if yea1 == "yes":
                        print("You have successfully recharged", "It will expire after 70 days", sep="\n")
                    else:
                      print("You have successfully canceled ordering")
                else:
                    print("Invalid input")
            elif rech == 2:
                sdec2 = ["1. 5$ for 30 Minutes", "2. 10$ for 60 Minutes", "3. 20$ for 120 Minutes", "4. 50$ for 300 Minutes"]
                for xx in sdec2:
                    print(xx)
                rech2 = int(input("Please Choose a number: "))
                if rech2 == 1:
                    yee = input("Are you sure you want to pay 5$ for 30 Minutes? (Yes or No): ").lower()
                    if yee == "yes":
                        print("You have successfully recharged", "It will expire after 2 weeks", sep="\n")
                    else:
                        print("You have successfully canceled ordering")
                elif rech2 == 2:
                    yaa = input("Are you sure you want to pay 10$ for 60 Minutes? (Yes or No): ").lower()
                    if yaa == "yes":
                        print("You have successfully recharged", "It will expire after 2 weeks", sep="\n")
                    else:
                        print("You have successfully canceled ordering")
                elif rech2 == 3:
                    yo = input("Are you sure you want to pay 20$ for 120 Minutes? (Yes or No): ").lower()
                    if yo == "yes":
                        print("You have successfully recharged", "It will expire after 30 days", sep="\n")
                    else:
                        print("You have successfully canceled ordering")
                elif rech2 == 4:
                    yoe = input("Are you sure you want to pay 50$ for 300 Minutes? (Yes or No): ").lower()
                    if yoe == "yes":
                        print("You have successfully recharged", "It will expire after 30 days", sep="\n")
                    else:
                        print("You have successfully canceled ordering")
                else:
                    print("Invalid input")

        #Internet Recharge Section

        elif userr == 3:
            sdec3 = ["1. 1$ for 2gb and 80 Minutes Airtime", "2. 0.5$ for 850mb and 30 Minutes Airtime", "3. 5$ for 12gb and 400 Minutes Airtime"]
            for yy in sdec3:
                print(yy)
            rech3 = int(input("Please Choose a number: "))
            if rech3 == 1:
                re = input("Are you sure you want 2gb internet and 80 Minutes Airtime for 1$? (Yes Or No): ")
                if re == "yes":
                    print("You have successfully recharged internet", "It will expire after 2 Weeks", sep="\n")
                else:
                     print("You have successfully canceled ordering")
            elif rech3 == 2:
                re2 = input("Are you sure you want 850mb internet and 30 Minutes Airtime for 0.5$? (Yes Or No): ")
                if re2 == "yes":
                    print("You have successfully recharged internet", "It will expire after 2 Weeks", sep="\n")
                else:
                    print("You have successfully canceled ordering")
            elif rech3 == 3:
                re3 = input("Are you sure you want 12gb internet and 400 Minutes Airtime for 5$? (Yes Or No): ")
                if re3 == "yes":
                    print("You have successfully recharged internet", "It will expire after 30 Days", sep="\n")
                else:
                    print("You have successfully canceled ordering")
            else:
                print("Invalid input")

        #Sending Money
        elif userr == 4:
            send = input("Please enter the Phone Number: ")
            if not send.isdigit():
                print("The phone Number can't contain letters")
            else:
                if len(send) > 9:
                    print("The number is greater than 9 digits")
                elif len(send) < 9:
                    print("The number is lesser than 9 digits")
                else:
                    money = float(input("Please enter an amount to send: "))
                    check = sim["balance"] - money
                    su = input(f"Are you sure to send {money:.2f}$ to {send}? (Yes or No): ").lower()
                    if not sim["balance"] > money:
                        print("Insufficient balance")
                    else:
                        if su == "yes":
                            print(f"You have successfully transferred {money:.2f}$ to {send}", f"You balance is: {check}",
                                  sep="\n")
                            sim["balance"] = check
                            with open("info.json", "w") as EVC:
                                json.dump(sim, EVC, indent=4)
                        else:
                            print("You have canceled the transaction")
         #Salaam Bank

        elif userr == 5:
            check1 = int(input("Please enter your bank pin: "))
            if check1 != sim["bpin"]:
                print("Incorrect pin")
            else:
                dicc = ["1. Show me My balance", "2. Deposit Money", "3. Withdraw Money", "4. Transfer Money to local Account", "5. Transfer Money to international Account"]
                for zz in dicc:
                    print(zz)
                om = int(input("Please choose a Number: "))
                if om == 1:
                    print(f"Your account balance is: {sim["b_balance"]:.2f}")
                elif om == 2:
                    dicc2 = ["1. Deposit from EVCplus Wallet", "2. Deposit from ATM"]
                    for k in dicc2:
                        print(k)
                    omm = int(input("Please choose a deposit method: "))
                    if omm == 1:
                        b_money = float(input("Please enter an amount to deposit: "))
                        kash = sim["balance"] - b_money
                        kash2 = sim["b_balance"] + b_money
                        su22 = input(f"Are you sure to deposit {b_money:.2f} to your bank account? (Yes or No): ").lower()
                        if su22 == "yes":
                            if not sim["balance"] >= b_money:
                                print("insufficient money")
                            else:
                                li = int(input("Please enter your bank pin to continue: "))
                                if li != sim["bpin"]:
                                    print("Incorrect pin")
                                else:
                                    sim["balance"] = kash
                                    sim["b_balance"] = kash2
                                    with open("info.json", "w") as EVC:
                                        json.dump(sim, EVC, indent=4)
                                    print(f"You have successfully deposited {b_money:.2f}$ to your bank account")
                                    print(f"Your bank account balance is: {kash2:.2f}")
                                    print(f"Your EVCplus wallet balance is: {kash:.2f}")
                    elif omm == 2:
                        code = random.randint(000000, 999999)
                        print("-" * 50)
                        print(f"Enter the following code to the ATM Deposit interface: {code}")
                        lo = float(input("Please enter the amount you want to deposit exactly as the ATM machine: "))
                        print("-" * 50)
                        print("Connecting...", "Please wait 5 seconds to verify your transaction", sep="\n")
                        #Testing ground

                        def count(end, start=0):
                            for xy in range(start, end + 1):
                                print(xy)
                                time.sleep(1)
                            print("We have verified your transaction")

                        count(5, 0)

                        # phone verification code
                        p_code = random.randint(00000, 99999)
                        print(f"Your verification code: {p_code}")
                        josh = int(input("Please enter the code that was sent to your phone number: "))

                        if not josh == p_code:
                            print()
                            print("The verification code that was provided is invalid")
                        else:
                            kass = sim["b_balance"] + lo
                            sim["b_balance"] = kass
                            with open("info.json", "w") as EVC:
                                json.dump(sim, EVC, indent=4)
                            print("-" * 50)
                            print(f"You have successfully deposited {lo:.2f}$ to your bank account")
                            print()
                            print(f"Your bank account balance is: {kass:.2f}")

                #ATM Withdraw

                elif om == 3:
                    dicc3 = ["1. Withdraw money to EVCplus Wallet", "2. Withdraw From ATM"]
                    for xyz in dicc3:
                        print(xyz)
                    nom = int(input("Please choose a Withdrawal method: "))
                    if nom == 1:
                        bk = float(input("Please Enter an amount to withdraw: "))
                        kaj = sim["b_balance"] - bk
                        kaj2 = sim["balance"] + bk
                        sy = input(f"Are your sure you want to Withdraw {bk:.2f} from your bank account? (Yes or No): ").lower()
                        if sy == "yes":
                            lks = int(input("Please enter your bank pin to continue: "))
                            if lks != sim["bpin"]:
                                print("Incorrect pin")
                            else:
                                if  bk > sim["b_balance"] :
                                    print("Insufficient Balance")
                                else:
                                    sim["balance"] = kaj2
                                    sim["b_balance"] = kaj
                                    with open("info.json", "w") as EVC:
                                        json.dump(sim, EVC, indent=4)
                                    print(f"You have successfully withdrawn {bk}$ from your bank account")
                                    print(f"Your bank account balance is: {kaj:.2f} ")
                                    print(f"You EVCplus balance is: {kaj2:.2f}")
                    elif nom == 2:
                        sudo = random.randint(00000, 99999)
                        print(f"Please Enter this code {sudo} into the ATM's Withdrawal interface")
                        lem = float(input("Enter an amount to withdraw: "))
                        print("Connecting...")
                        def count1(end2, start2=0):
                            for uz in range(start2, end2 + 1):
                                print(uz)
                                time.sleep(1)
                            print("We have verified your transaction")
                        count1(5, 0)

                        #Withdraw Phone Verification
                        p2_code = random.randint(00000, 99999)
                        print(f"Your verification code: {p2_code}")
                        jon = int(input("Please enter the code that was sent to your phone number: "))

                        if not jon == p2_code:
                            print("Invalid Verification code")
                        else:
                            kae = sim["b_balance"] - lem
                            sim["b_balance"] = kae
                            with open("info.json", "w") as EVC:
                                json.dump(sim, EVC, indent=4)
                            print("-" * 50)
                            print(f"You have successfully withdrawn {lem:.2f}$ from your bank account")
                            print()
                            print(f"Your bank account balance is: {kae:.2f}")

                #Local Transfer
                elif om == 4:
                    lmt = input("Please Enter account Number: ")
                    if not lmt.isdigit():
                        print("Account Number cannot contain letters")
                    else:
                        if len(lmt) >= 9:
                            print("Account number exceeds 8 digits")
                        elif len(lmt) <= 7:
                            print("Account number cannot be less than 8 digits")
                        else:
                            lmm = float(input("Please enter an amount to transfer: "))
                            ramz = int(input("Please enter your pin to confirm transaction: "))
                            if ramz != sim["bpin"]:
                                print("Incorrect pin")
                            else:
                                t2k = input(f"Are you sure to transfer {lmm:.2f}$ to {lmt}? (Yes or No): ").lower()
                                if t2k == "yes":
                                    if  lmm > sim["b_balance"]:
                                        print("Insufficient balance")
                                    else:
                                        folos = sim["b_balance"] - lmm
                                        sim["b_balance"] = folos
                                        with open("info.json", "w") as EVC:
                                            json.dump(sim, EVC, indent=4)
                                        print(f"You have successfully transferred {lmm:.2f}$ to {lmt} ")
                                        print()
                                        print(f"Your bank account balance is: {folos:.2f} ")
                                else:
                                    print("-" * 50)
                                    print("You have cancelled the transaction successfully.")

                #International Transfer
                elif om == 5:
                    imt = input("Please enter account Number: ")
                    if not imt.isdigit():
                        print("Account number cannot contain letters")
                    else:
                        if len(imt) >= 12:
                            print("Account number cannot exceed 11 digits")
                        elif len(imt) <= 10:
                            print("Account number cannot be less than 11 digits")
                        else:
                            lm2 = float(input("Please enter an amount to transfer: "))
                            ramz2 = int(input("Please enter your pin to confirm transaction: "))
                            if ramz2 != sim["bpin"]:
                                print("Incorrect pin")
                            else:
                                t3l = input(f"Are sure to trnasfer {lm2:.2f}$ to {imt}? (Yes or No): ").lower()
                                if t3l == "yes":
                                    if lm2 > sim["b_balance"]:
                                        print("insuffecient Balance")
                                    else:
                                        folo = sim["b_balance"] - lm2
                                        sim["b_balance"] = folo
                                        with open("info.json", "w") as EVC:
                                            json.dump(sim, EVC, indent=4)
                                        print(f"You have successfully transferred {lm2:.2f}$ to {imt}")
                                        print()
                                        print(f"Your bank account balance is: {folo:.2f} ")
                                else:
                                    print("-" * 50)
                                    print("You have cancelled the transaction successfully.")

                elif om == 6:
                    print("Enter a 6 digits number pin")
                    new_bpin = int(input("Enter your new pin: "))
                    new_bpin2 = int(input("Enter your new pin again: "))
                    if new_bpin != new_bpin2:
                        print("Pin is incorrect/ Make sure you entered correct pin")
                    else:
                        if 99999 <= new_bpin <= 1000000:
                            print("Pin must be exactly 6 digis")
                        else:
                            sim["bpin"] = new_bpin
                            with open("info.json", "w") as EVC:
                                json.dump(sim, EVC, indent=4)
                            print("You have changed your pin successfully")

         #change EVC Pin
        elif userr == 6:
            print("Ener a 4 digits number pin")
            new_pin = int(input("Enter Your new Pin: "))
            new_pin2 = int(input("Enter Your new Pin again: "))
            if not new_pin == new_pin2:
                print("Pin is incorrect. Make sure you entered correct pin")
            else:
                if 1000 <= new_pin and new_pin2 <= 9999:
                    sim["pin"] = new_pin
                    with open("info.json", "w") as EVC:
                        json.dump(sim, EVC, indent=4)
                    print("You have changed your pin successfully")
                else:
                    print("PIN must be exactly 4 digits")


    print()
    ask = input("Press Q to Quit or press Enter to Continue: ").lower()
    if ask == "q":
        running = False



















