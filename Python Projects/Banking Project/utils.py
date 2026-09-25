import json

def load():
    with open("data/custormers.json", "r") as file:
        return json.load(file)
def save(dat):
    with open("data/custormers.json", "w") as file:
        json.dump(dat, file, indent = 4)
dat = load()
