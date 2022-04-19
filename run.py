"""
import pygiglet to style the game title
"""
import random
import pyfiglet


gametitle = pyfiglet.figlet_format("Enigma", font="isometric1")
print(gametitle)


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
