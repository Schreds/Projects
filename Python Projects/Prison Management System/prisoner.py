import random
from utils import load, save
PRISONERS_FILE = "data/prisoners.json"

class Prisoner:
    def __init__(self, prisoner_id, name, age, gender, dob, pob, arrest_date,arrest_city, arrest_state, crime, crime_description, sentence_length, release_date, security_classification):
        self.prisoner_id = prisoner_id
        self.name = name
        self.age = age
        self.gender = gender
        self.dob = dob
        self.pob = pob

        self.arrest_date = arrest_date
        self.arrest_city = arrest_city
        self.arrest_state = arrest_state

        self.crime = crime
        self.crime_description = crime_description

        self.sentence_length = sentence_length
        self.release_date = release_date

        self.security_classification = security_classification

        self.status = "IN_CUSTODY"
        self.cell_num = None
        self.num_incidents = 0

    def show_info(self):
        print("\n--- Prisoner Information ---")
        print(f"Prisoner ID: {self.prisoner_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Date of Birth: {self.dob}")
        print(f"Place of Birth: {self.pob}")
        print(f"Crime: {self.crime}")
        print(f"Sentence: {self.sentence_length}")
        print(f"Release Date: {self.release_date}")
        print(f"Security Classification: {self.security_classification}")
        print(f"Status: {self.status}")
        print(f"Cell: {self.cell_num}")
        print(f"Incidents: {self.num_incidents}")

    def to_dict(self):
        return {
            #Prisoners Info
            "Prisoner_id": self.prisoner_id,
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Date_Of_Birth": self.dob,
            "Place_Of_Birth": self.pob,

            #Arrest Date, City and State
            "Arrest_Date": self.arrest_date,
            "Arrest_City": self.arrest_city,
            "Arrest_State": self.arrest_state,

            #Crime Commited
            "Crime": self.crime,
            "Crime_Description": self.crime_description,

            #Sentence length and Release date
            "Sentence_Length": self.sentence_length,
            "Release_Date": self.release_date,

            #Threat Level
            "Security_Classification": self.security_classification,

            #Status, Cell Number and Number of Incidents
            "Status": self.status,
            "Cell_Num": self.cell_num,
            "Num_Incidents": self.num_incidents
        }

def generate_prisoner_id(prisoners):
    while True:
        prisoner_id = f"SV-{random.randint(1, 99999):05d}"
        found = False

        for prisoner in prisoners:
            if prisoner["Prisoner_id"] == prisoner_id:
                found = True
                break
        if not found:
            return prisoner_id

def register_prisoner():
    prisoners = load(PRISONERS_FILE)
    prisoner_id = generate_prisoner_id(prisoners)

    print("\n--- Prisoner Registration ---")
    name = input("Enter The Full Name: ")
    if name == "":
        print("Name Cannot be Empty")
        return
    try:
        age = int(input("Enter the Age: "))
        if age < 17:
            print("You Cannot Register Minors!")
            return
    except ValueError:
        print("Age must be a number")
        return None
    gender = input("Enter the Gender (Male/female): ").lower()
    if gender == "":
        print("Gender Cannot Be Empty.")
        return
    if gender not in ("male", "female"):
        print("Invalid Gender")
        return None
    dob = input("Enter the Date Of Birth: ")
    if dob == "":
        print("Date Of Birth Cannot be Empty, Please use this format: (xx/xxx/xxxx)")
        return
    if len(dob) < 11:
        print("Date Of Birth Cannot be Empty, Please use this format: (xx/xxx/xxxx)")
        return
    pob = input("Enter Place of birth: ")
    if pob == "":
        print("Place of Birth Cannot be Empty.")
        return
    arrest_date = input("Enter The Arrest Date (xx/xxx/xxxx): ")
    if arrest_date == "":
        print("Arrest Date is Invalid, Please use this format: (xx/xxx/xxxx)")
        return
    if len(arrest_date) < 11:
        print("Arrest Date is Invalid, Please use this format: (xx/xxx/xxxx)")
        return
    arrest_city = input("Arrested In which City?: ")
    if arrest_city == "":
        print("Arrest City Cannot be Empty.")
        return
    arrest_state = input("Arrested In which State?: ")
    if arrest_state == "":
        print("Arrest State Cannot Be Empty.")
        return
    crime = input("Enter the Crime Commited: ")
    if crime == "":
        print("The Crime field Cannot be Empty.")
        return
    crime_description = input("Enther the Crime Description: ")
    if crime_description == "":
        print("Crime Description Cannot Be Empty.")
        return
    sentence_length = input("Enter the Sentence Length: ")
    if sentence_length == "":
        print("Sentence Length Cannot Be Empty.")
        return
    release_date = input("Enter the Release Date (xx/xxx/xxxx): ")
    if release_date == "":
        print("Invalid Release Date, Please use this format: (xx/xxx/xxxx)")
        return
    if len(release_date) < 11:
        print("Invalid Release Date, Please use this format: (xx/xxx/xxxx)")
        return

    try:
        security_classification = int(input("Enter The Prisoner Security Classification (1-4): "))
    except ValueError:
        print("Security Classification must be a number.")
        return

    if security_classification not in (1,2,3,4):
        print("Security Classification must be between 1 and 4.")
        return

    prisoner = Prisoner(
        prisoner_id,
        name,
        age,
        gender,
        dob,
        pob,
        arrest_date,
        arrest_city,
        arrest_state,
        crime,
        crime_description,
        sentence_length,
        release_date,
        security_classification
    )
    prisoners.append(prisoner.to_dict())
    save(PRISONERS_FILE, prisoners)
    print("\nPrisoner Registered Successfully")
    print(f"Prisoner ID: {prisoner.prisoner_id}")

    return prisoner


