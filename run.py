# import packages to add to program
import random
from termcolor import colored
from pyfiglet import Figlet


def secret_code(max_range):
    """
    Generate random 4 number code
    """
    secret_code = []
    for i in range(4):
        secret_code.append(random.randint(1, max_range))
    return secret_code


enigma_code = secret_code(10)
print(enigma_code)
f = Figlet(font='banner3-D')
print(colored(f.renderText('ENIGMA'), 'red'))


# Enigma game will run below here
f = Figlet(font='digital')
print(colored(f.renderText('Can you crack the code'), 'green'))
print("Guess all 4 numbers to crack the ENIGMA code!\n")


# Variable to store the correct guesses and attempts
correct = 0
attempts = 0


# Variables to store the players guesses
while correct < 4:
    attempt1 = int(input("Please guess the first number: "))
    attempt2 = int(input("Please guess the second number: "))
    attempt3 = int(input("Please guess the third number: "))
    attempt4 = int(input("Please guess the fourth number: "))
    attempts += 1

    if attempt1 == enigma_code[0]:
        correct += 1
    if attempt2 == enigma_code[1]:
        correct += 1
    if attempt3 == enigma_code[2]:
        correct += 1
    if attempt4 == enigma_code[3]:
        correct += 1

    if correct < 4:
        print("\nYou cracked " + str(correct) + " numbers correctly\n")
        correct = 0
        continue
    else:
        if attempts == 1:
            print("\nCongratulations you cracked the Enigma code!!" +
                  "You did it in " + str(attempts) + " try.\n")
        else:
            print("\nCongratulations you cracked the Enigma code!!" +
                  "You did it in " + str(attempts) + " tries.\n")
