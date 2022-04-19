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


enigma_code = secret_code(50)
print(enigma_code)

# Enigma game will run below here
game_title = pyfiglet.figlet_format("Enigma", font="isometric1")
print(game_title)
print("\nWelcome to the Enigma!!!\n")
print("Can you crack the code and win the war\n")
print("Guess all 4 numbers in the correct location to crack the enigma code!!!\n")
