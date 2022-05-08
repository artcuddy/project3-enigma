""" ENIGMA Game import packages to add to program """
# import os to help clear terminal
import os

# import termcolor for adding colour to text
from termcolor import colored

# import pyfiglet for ascii art
from pyfiglet import Figlet

# import player class
from player import Player

# import code class
from codegen import Code


def clear_game():
    """
    Clear screen to enable new game play
    """
    os.system("clear")


# print(code.get_code_input)
heading = Figlet(font='banner3-D')
print(colored(heading.renderText('ENIGMA'), 'red'))


def welcome():
    """
    ENIGMA Title & welcome message
    """
    sub_heading = Figlet(font='digital')
    print(colored(sub_heading.renderText('Can you crack the code'), 'green'))
    print("Guess all 4 numbers to crack the ENIGMA code!\n")


def main():
    """
    Run all program functions and methods
    """
    welcome()

    player = Player()

    code = Code()

    # calling the methods in the Code class
    secret_code = code.random_code(10)
    print(secret_code)

    # calling the methods in the Player class
    player.get_player_name()
    player.game_control()
    player.start_game()


if __name__ == '__main__':
    main()
