"""
#import pygiglet to style the game title
"""
import random
import pyfiglet


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
game_title = pyfiglet.figlet_format("Enigma", font="isometric1")
print(game_title)


# Enigma game will run below here
welcome = pyfiglet.figlet_format("Welcome to the Enigma", font="digital")
print(welcome + "\n")
print("Can you crack the code and win the war\n")
print("Guess all 4 numbers to crack the enigma code!\n")


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
            print("\nCongratulations you cracked the Enigma code!! You did it in " + str(attempts) + " try.\n")
        else:
            print("\nCongratulations you cracked the Enigma code!! You did it in " + str(attempts) + " tries.\n")
