"""
As a user, I want to use a program which can generate random password and display the result on user interface.
So that I can generate my password for any application.
Acceptance Criteria:
Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
You must import some required modules or packages. The GUI of program must contain at least a button and a label.
The result should be display on the password label when the user click the generate button.
"""

import random
import string


def generatePassword():
    myPass = set()
    while len(myPass) < 2:
        myPass.add(random.choice(string.ascii_uppercase))

    while len(myPass) < 4:
        myPass.add(random.choice(string.digits))

    while len(myPass) < 6:
        myPass.add(random.choice(string.punctuation))

    while len(myPass) < 10:
        myPass.add(random.choice(string.ascii_letters))

    return print(''.join(myPass))


print("Welcome to password generator")
print("here is your password")
generatePassword()
