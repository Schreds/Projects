import random
import string
import json

def load():
    with open("Abood.json", "r") as file:
         return json.load(file)
upload = load()

def save(upload):
    with open("Abood.json", "w") as file:
        json.dump(upload, file, indent = 4)

chars = " " + string.ascii_letters + string.digits + string.punctuation
long = list(chars)
key = long.copy()
random.shuffle(key)

print("1. Encrypt a message", "2. Decrypt a message", sep = "\n")
user = int(input("Choose a number: "))

def encryption():
    enc_text = input("Enter a message to encrypt: ")
    ciph_text = ""

    for letter in enc_text:
        index = long.index(letter)
        ciph_text += key[index]

    guy = {
        "Encrypted": ciph_text,
        "Decryption_Key": "".join(key)
    }

    upload["encryped"].append(guy)
    save(upload)
    #print(f"original Message: {enc_text}")
    #print(f"enc message: {ciph_text}")

def decryption():
    dec_text = input("Enter the decryption code to decrypt a message: ")
    plain_text = ""

    for mess in upload["encryped"]:

        if mess["Encrypted"] == dec_text:

            key = mess["Decryption_Key"]

            for letter in dec_text:
                index = key.index(letter)
                plain_text += long[index]

            print(f"Original Message: {plain_text}")


            guh = {
                "Dycrypted" : plain_text,
                "Encryption Code" : dec_text,
                "Decryption_Key" : "".join(key)
            }
            upload["decrypted"].append(guh)
            save(upload)
            return
    print("Encrypted message not found.")

    '''Make sure to delete the decrypted message after someone uses the encryption key to see the message. '''

if user == 1:
    encryption()
elif user == 2:
    decryption()
else:
    print("Invalid Number")