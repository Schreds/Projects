import json

with open("Abood2.json", "r") as kind:
    crash = json.load(kind)

def ntask():
    menu = ["1. New Task", "2. View Tasks", "3. Remove Tasks"]
    for m in menu:
        print(m)
    print("-" * 50)
    opt = int(input("Choose a number: "))
    print()
    if opt == 1:
        new_task = input("Enter a new task: ")
        desc = input("Enter a description for the task: ")
        if new_task != "" and desc != "":
            Task = {
                "Task": new_task,
                "Description": desc
            }
            crash.append(Task)
            with open("Abood2.json", "w") as kind:
                        json.dump(crash, kind, indent = 4)
            print("Task Has been added")
        else:
             print("Task and Description can not be empty")
        

    elif opt == 2:
        for number ,i in enumerate(crash, start=1):
            print(f"#{number}.Task: ")
            print(f"Task: {i['Task']}")
            print(f"Description: {i['Description']}")
            print()

    
    elif opt == 3:
        #if len(crash) == 0:
         #print("There are no to remove")

         for number, i in enumerate(crash, start = 1):
            print(f"#{number}.Task: ")
            print(f"Task {i['Task']}")
            print(f"Descritpion: {i['Description']}")
            print()
         ask = int(input("Which task would you like to remove?: "))
         if 1 <= ask <= len(crash):
            crash.pop(ask - 1)

            with open("Abood2.json", "w") as kind:
                json.dump(crash, kind, indent=4)

            print("Task removed successfully")
         else:
              print("Invalid Task Number")


ntask()