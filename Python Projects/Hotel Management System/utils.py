import json

def load():
    with open("data/reservations.json", "r") as file:
        return json.load(file)
def save(det):
    with open("data/reservations.json", "w") as file:
        json.dump(det, file, indent = 4)

def load2():
    with open("data/rooms.json", "r") as file:
        return json.load(file)
def save2():
    with open("data/rooms.json", "w") as file:
        json.dump(rom, file, indent = 4)

det = load()
rom = load2()