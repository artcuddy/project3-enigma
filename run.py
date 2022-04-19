"""
import pygiglet to style the game title
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

# Variables to store the palyers guesses
attempt1 = int(input("Please guess the first number: "))
attempt2 = int(input("Please guess the second number: "))
attempt3 = int(input("Please guess the third number: "))
attempt4 = int(input("Please guess the fourth number: "))
