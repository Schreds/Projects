from utils import det, save, rom
import random
import time


def single(guest_info):

    price = 45.75

    while True:

        ke = su("single_bed")

        j = input(
            f"Did you like room Number: {ke}? (Y/N): "
        ).lower()

        if j == "":
            print("Please Answer with either Y Or N")
            return
        if j == "y":

            ka = key()
            klp = ref()

            num_nights = guest_info["Number_Of_Nights"]

            tot = num_nights * price

            guest_info["Room_Type"] = "Single Bed"

            guest_info["Room_Number"] = ke

            guest_info["Room_Password"] = ka

            guest_info["Floor"] = 1

            guest_info["Price_Per_Night"] = price

            guest_info["Reference_Number"] = klp

            guest_info["Total_Price"] = tot

            det["Cus_Info"].append(guest_info)

            save(det)

            print()
            print(
                "Thank You for staying with us.",
                f"Your room number is: #{ke} 1st Floor",
                f"And the Password for the room is: {ka}",
                f"Your reference Number is: {klp}",
                sep="\n"
            )
            print(f"Total price: ${tot:.2f}")
            return

        if j == "n":
            print("Picking Another Room...")
            count(0, 2)
        else:
            print("Invalid Answer")

def double(guest_info):

    price = 55.50

    while True:

        ke = su("double_bed")

        j = input(
            f"Did you like room Number: {ke}? (Y/N): "
        ).lower()

        if j == "":
            print("Please Answer with either Y Or N")
            return

        if j == "y":

            ka = key()
            klp = ref()

            num_nights = guest_info["Number_Of_Nights"]

            tot = num_nights * price

            guest_info["Room_Type"] = "Double Bed"

            guest_info["Room_Number"] = ke

            guest_info["Room_Password"] = ka

            guest_info["Floor"] = 2

            guest_info["Price_Per_Night"] = price

            guest_info["Reference_Number"] = klp

            guest_info["Total_Price"] = tot

            det["Cus_Info"].append(guest_info)

            save(det)

            print()
            print(
                "Thank You for staying with us.",
                f"Your room number is: #{ke} 2nd Floor",
                f"And the Password for the room is: {ka}",
                f"Your reference Number is: {klp}",
                sep="\n"
            )
            print(f"Total price: ${tot:.2f}")
            return
        if j == "n":

            print("Picking Another Room...")

            count(0, 2)
        else:

            print("Invalid Answer")

def twin(guest_info):

    price = 69.99

    while True:

        ke = su("twin_bed")

        j = input(
            f"Did you like room Number: {ke}? (Y/N): "
        ).lower()

        if j == "":
            print("Please Answer with either Y Or N")
            return
        if j == "y":

            ka = key()
            klp = ref()

            num_nights = guest_info["Number_Of_Nights"]

            tot = num_nights * price

            guest_info["Room_Type"] = "Twin Bed"

            guest_info["Room_Number"] = ke

            guest_info["Room_Password"] = ka

            guest_info["Floor"] = 3

            guest_info["Price_Per_Night"] = price

            guest_info["Reference_Number"] = klp

            guest_info["Total_Price"] = tot

            det["Cus_Info"].append(guest_info)

            save(det)

            print()
            print(
                "Thank You for staying with us.",
                f"Your room number is: #{ke} 3rd Floor",
                f"And the Password for the room is: {ka}",
                f"Your reference Number is: {klp}",
                sep="\n"
            )

            print(f"Total price: ${tot:.2f}")

            return
        if j == "n":

            print("Picking Another Room...")

            count(0, 2)
        else:

            print("Invalid Answer")

def family(guest_info):

    price = 86.25

    while True:

        ke = su("family_bed")

        j = input(
            f"Did you like room Number: {ke}? (Y/N): "
        ).lower()

        if j == "":
            print("Please Answer with either Y Or N")
            return
        if j == "y":

            ka = key()
            klp = ref()

            num_nights = guest_info["Number_Of_Nights"]

            tot = num_nights * price

            guest_info["Room_Type"] = "Family Room"

            guest_info["Room_Number"] = ke

            guest_info["Room_Password"] = ka

            guest_info["Floor"] = 4

            guest_info["Price_Per_Night"] = price

            guest_info["Reference_Number"] = klp

            guest_info["Total_Price"] = tot

            det["Cus_Info"].append(guest_info)

            save(det)

            print()
            print(
                "Thank You for staying with us.",
                f"Your room number is: #{ke} 4th Floor",
                f"And the Password for the room is: {ka}",
                f"Your reference Number is: {klp}",
                sep="\n"
            )

            print(f"Total price: ${tot:.2f}")

            return
        if j == "n":

            print("Picking Another Room...")

            count(0, 2)
        else:

            print("Invalid Answer")

def president(guest_info):

    price = 135.99

    while True:

        ke = su("president")

        j = input(
            f"Did you like room Number: {ke}? (Y/N): "
        ).lower()

        if j == "":
            print("Please Answer with either Y Or N")
            return

        if j == "y":

            ka = key()
            klp = ref()

            num_nights = guest_info["Number_Of_Nights"]

            tot = num_nights * price

            guest_info["Room_Type"] = "Presidential Suite"

            guest_info["Room_Number"] = ke

            guest_info["Room_Password"] = ka

            guest_info["Floor"] = 5

            guest_info["Price_Per_Night"] = price

            guest_info["Reference_Number"] = klp

            guest_info["Total_Price"] = tot

            det["Cus_Info"].append(guest_info)

            save(det)
            print()
            print(
                "Thank You for staying with us.",
                f"Your room number is: #{ke} 5th Floor",
                f"And the Password for the room is: {ka}",
                f"Your reference Number is: {klp}",
                sep="\n"
            )

            print(f"Total price: ${tot:.2f}")

            return
        if j == "n":

            print("Picking Another Room...")

            count(0, 2)
        else:

            print("Invalid Answer")

def su(room_type):
    rooms = rom["Rooms"][0][room_type]
    room = random.choice(rooms)
    return room

def count(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)

def key():
    password = f"{random.randint(0, 9999):04d}"
    return password

def ref():
    refr = f"{random.randint(0, 99999):05d}"
    return refr