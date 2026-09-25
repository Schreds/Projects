from Customer import login
from Customer import ours
from account import create


def main():

    print("Welcome to CBS Bank")

    print(
        "\n1. Login to your Bank account",
        "2. Open account with CBS Bank",
        sep="\n"
    )
    user = int(input("Please choose a number: "))

    if user == 1:
        account = login()
        if account is not None:

            print("You have successfully Logged in.")
            ours(account)
        else:
            print("Username or Password is incorrect.")
    elif user == 2:
        create()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
