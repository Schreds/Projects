def ltm(account):
    acc_num = input("Please enter account number: ")
    if not acc_num.isdigit():
        print("Account Number Cannot contain letters or special characters")
    else:
        if len(acc_num) <= 7 or len(acc_num) >= 9:
            print("The account number cannot be greater than or lesser than 8 digits")
        else:
            acc_money = float(input("Enter an amount to transfer: "))
            if acc_money <= 0:
                print("Invalid amount, the value must be greater than 0")
            else:
                master = account["master"][0]
                bpin = input("Please enter your pin to verify the transaction: ")
                if bpin != master["pin"]:
                    print("Invalid Pin.")
                else:
                    if acc_money > master["balance"]:
                        print("insufficient Balance")
                    else:
                        fee = acc_money * 0.0
                        total = acc_money + fee

                        master["balance"] -= total

                        reference = random.randint(0, 99999)
                        te = {
                            "Transaction_Type": "Transfer",
                            "Account_Number": acc_num,
                            "Amount_Transferred": acc_money,
                            "Date": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
                            "Reference_Number": reference,
                            "Transferring_Service": "Local",
                            "Transfer_Fees": fee
                        }
                        account["Transaction_History"].append(te)

                        save(dat)
                        print(
                            f"You have successfully transferred ${acc_money:.2f} to {acc_num}",
                            f"Transferring fees are: ${fee:.2f}",
                            f"Your new Balance is: ${master['balance']:.2f}",
                            sep="\n"
                        )