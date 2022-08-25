import string
from random import choice, shuffle

def randomPass():
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    

    allCharacters = lower + upper + digits
    shuffle(allCharacters)

    length = int(input("How long would you like the password to be? "))
    password = ''

    for i in range(length):
        password += choice(allCharacters)
    
    print(password)

randomPass()

