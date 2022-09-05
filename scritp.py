import string
import random


alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():

    length = int(input("Inserire la lunghezza della password: "))
    alphabets_count = int(
        input("Inserire il numero di lettere presenti nella password: "))
    digits_count = int(
        input("Inserire il numero di cifre presenti nella password: "))
    special_characters_count = int(
        input("Inserire il numero di caratteri speciali presenti nella password: "))

    characters_count = alphabets_count + digits_count + special_characters_count

    if characters_count > length:
        print("Il conteggio totale dei caratteri è maggiore della lunghezza della password")
        return

    password = []

    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))


generate_random_password()
