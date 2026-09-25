from reservation import reser

def main():
    print("\n" + "=" * 44)
    print("       Welcome To Kindro Grand Hotel")
    print("=" * 44)
    print()
    print("1. Reservations")
    print("2. Guests")
    print("3. Rooms")
    print("4. Check In")
    print("5. Check Out")
    cho = input("Choose a number: ")
    if not cho.isdigit():
        print("You can only use digits")
        return
    if cho == "1":
        reser()
        return
    if cho == "2":
        pass
        return
    if cho == "3":
        pass
        return
    if cho == "4":
        pass
        return
    if cho == "5":
        pass
        return
if __name__ == "__main__":
    main()