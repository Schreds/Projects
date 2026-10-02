import random
from utils import load, save

WORKERS_FILE = "data/workers.json"

class Worker:
    def __init__(self, worker_id, name, age, gender ,occupation, security_level):
        self.worker_id = worker_id
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.security_level = security_level
        self.active = True

    def show_info(self):
        print("\n--- Worker Information ---")
        print(f"Worker ID: {self.worker_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")
        print(f"Security Level: {self.security_level}")
        print(f"Active: {self.active}")

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def to_dict(self):
        return {
            "Worker_ID": self.worker_id,
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Occupation": self.occupation,
            "Security_Level": self.security_level,
            "Active": self.active
        }

def generate_worker_id(workers):
    while True:
        worker_id = f"WR-{random.randint(1, 99999):05d}"
        found = False
        for worker in workers:
            if worker["Worker_ID"] == worker_id:
                found = True
                break
        if not found:
            return worker_id

def register_worker():
    workers = load(WORKERS_FILE)

    worker_id = generate_worker_id(workers)

    print("\n--- Worker Registration ---")
    name = input("Enter Worker's Full Name: ")
    if name == "":
        print("Name Cannot Be Empty.")
        return
    if name.isdigit():
        print("Cannot Cannot Be Digits.")
        return
    try:
        age = int(input("Enter Worker's Age: "))
    except ValueError:
        print("Age Must Be a Number.")
        return
    if age < 18:
        print("You Cannot Hire Minors!")
        return
    gender = input("Enter the Worker's Gender (Male/Female): ").lower()
    if gender == "":
        print("Gender Cannot Be Empty.")
        return
    if gender not in ("male", "female"):
        print("Invalid Gender.")
        return
    occupation = input("Enter The Occupation: ")
    if occupation == "":
        print("Occupation Cannot Be Empty.")
        return

    print("\nSecurity Levels:")
    print("1. Support Staff")
    print("2. Guard/ Registration Officer")
    print("3. Warden")
    print("4. Administrator")

    try:
        security_level = int(input("Enter The Security Level (1-4): "))
    except ValueError:
        print("Security Level Must Be Between 1 and 4.")
        return
    if security_level not in (1,2,3,4):
        print("Security Level Must Be Between 1 and 4")
        return

    worker = Worker(worker_id, name, age, gender, occupation, security_level)

    workers.append(worker.to_dict())
    save(WORKERS_FILE,workers)

    print("\nWorker Was Registered Successfully.")
    print(f"Worker's ID: {worker.worker_id}")

    return worker

