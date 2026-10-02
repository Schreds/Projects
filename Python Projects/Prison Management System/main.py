from prisoner import register_prisoner
from utils import load
from worker import register_worker
PRISONERS_FILE = "data/prisoners.json"
WORKERS_FILE = "data/workers.json"

def view_prisoners():
    prisoners = load(PRISONERS_FILE)

    if len(prisoners) == 0:
        print("\nNo Prisoners Registered")
        return
    print("\n--- Registered Prisoners ---")

    for number, prisoner in enumerate(prisoners, start = 1):

        print()
        print(f"Prisoners Information #{number}")
        print(f"ID: {prisoner['Prisoner_id']}")
        print(f"Name: {prisoner['Name']}")
        print(f"Crime: {prisoner['Crime']}")
        print(f"Status: {prisoner['Status']}")

def view_workers():
    workers = load(WORKERS_FILE)
    if len(workers) == 0:
        print("\nNo Workers Registered")
        return

    print("\n--- Registered Workers ---")

    for number, worker in enumerate(workers, start = 1):
        print()
        print(f"Worker Information #{number}")
        print(f"ID: {worker['Worker_ID']}")
        print(f"Name: {worker['Name']}")
        print(f"Age: {worker['Age']}")
        print(f"Occupation: {worker['Occupation']}")
        print(f"Security Level: {worker['Security_Level']}")
        print(f"Active: {worker['Active']}")

def main():
    while True:
        print("\n==============================")
        print("   PRISON MANAGEMENT SYSTEM")
        print("==============================")

        print("1. Register Prisoner")
        print("2. View Prisoners")
        print("3. Register New Worker")
        print("4. View Workers")
        print("0. Exit")
        choice = input("Choose a Number: ")
        if choice == "1":
            register_prisoner()
        elif choice == "2":
            view_prisoners()
        elif choice == "3":
            register_worker()
        elif choice == "4":
            view_workers()
        elif choice == "0":
            print("System Closed.")
            break
        else:
            print("Invalid Choice.")
main()
