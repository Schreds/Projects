from utils import *
from rooms import single, double, twin, family, president


def reser():
    print("1. Passport")
    print("2. Identification Card")

    id = input("Which Document are you trying to provide?: ")

    if not id.isdigit():
        print("Invalid Choice")
        return

    if id == "1":
        passport()
        return

    if id == "2":
        Identi()
        return

    print("Invalid Choice")

def user_info(Doc_Type, iden):

    nm = input("Enter your Full name: ")

    if nm == "":
        print("Name Cannot be empty")
        return

    dt = input("Enter the date you will be check-in (xx/Jan/xxxx): ")

    if dt == "":
        print("Check-in date cannot be empty")
        return

    if len(dt) <= 10:
        print("Invalid check-In details. Please use this format: (xx/Jan/xxxx)")
        return

    phone = input("Enter your phone Number: ")

    if phone == "":
        print("Phone Number Cannot be Empty")
        return

    if not phone.isdigit():
        print("Phone Number must be digits")
        return

    email = input("Enter Your Email Address: ")

    if email == "":
        print("Email Address cannot be empty")
        return

    dob = input("Enter your date of birth: ")

    if dob == "":
        print("Date of birth cannot be empty")
        return

    if len(dob) <= 10:
        print("Invalid Date of Birth details. Please use this format: (xx/Jan/xxxx)")
        return

    num_adult = input("Enter number of adults: ")

    if num_adult == "":
        print("Please make sure to provide the Number of adults.")
        return

    if not num_adult.isdigit():
        print("Number of adults must be digits.")
        return

    if int(num_adult) <= 0:
        print("There must be at least one adult.")
        return

    num_chi = input("Enter the number of children: ")

    if num_chi == "":
        print("Please make sure to provide the Number of children.")
        return

    if not num_chi.isdigit():
        print("Number of children must be digits.")
        return

    num_nights = input("How Many nights would you like to stay?: ")

    if not num_nights.isdigit():
        print("Number of nights must be digits.")
        return

    num_nights = int(num_nights)

    if num_nights <= 0:
        print("Please enter valid information.")
        return

    dto = input("Enter Check-Out Date: ")

    if dto == "":
        print("Check-Out date Cannot be empty.")
        return

    if len(dto) <= 10:
        print("Invalid check-Out details. Please use this format: (xx/Jan/xxxx)")
        return

    guest_info = {
        "Name": nm,
        "Phone_Number": phone,
        "Email_Address": email,
        "Document_Type": Doc_Type,
        "Document_ID_Number": iden,
        "Date_Of_Birth": dob,
        "Number_Of_Nights": num_nights,
        "Number_Of_Adults": int(num_adult),
        "Number_Of_Children": int(num_chi),
        "Check-in": dt,
        "Check-Out": dto
    }

    print(
        "1. Single Bed",
        "2. Double Bed",
        "3. Twin Bed",
        "4. Family Room",
        "5. Presidential Suite",
        sep="\n"
    )

    room_type = input("Choose a room type: ")

    if not room_type.isdigit():
        print("You cannot use Letter or word, only use digits.")
        return

    if room_type == "1":
        single(guest_info)
        return

    if room_type == "2":
        double(guest_info)
        return

    if room_type == "3":
        twin(guest_info)
        return

    if room_type == "4":
        family(guest_info)
        return

    if room_type == "5":
        president(guest_info)
        return

    print("Invalid Number")

def passport():
    Doc_Type = "Passport"
    char = input(
        "Enter the first Character of your passport "
        "(if there is no letter just hit enter): "
    ).upper()
    if len(char) >= 2:
        print(
            "Invalid Character, Please Provide the First letter "
            "of your passport if there is"
        )
        return
    id_num = input("Enter your Passport Number: ")
    if not id_num.isdigit():
        print("Passport Number must be digits")
        return
    if len(id_num) <= 7:
        print(
            "Passport Number is incorrect, Make sure that "
            "Your passport number is more than 8 digits"
        )
        return
    iden = char + id_num

    user_info(Doc_Type, iden)

def Identi():
    Doc_Type = "Identification Card"
    iden = input("Enter Your Identification Card Number: ")
    if not iden.isdigit():
        print("Identification Number must be digits")
        return
    if len(iden) <= 7:
        print("Identification Number must be greater than 8 digits")
        return

    user_info(Doc_Type, iden)

