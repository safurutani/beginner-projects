import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def gen_pass():
    password_length = int(input("How many characters would you like in your password?\n"))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    print(password)

gen_pass()