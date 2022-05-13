""" Main Game Control """
# import os to help clear terminal
import os

# import termcolor for adding colour to text
from termcolor import colored

# import player class
from player import Player

# import player class
from codegenerator import Codegen

# import player class
from attempts import Attempts

# import player class
from game import Welcome


class Newgame:
    """
    Start new game
    """
    @staticmethod
    def start_new_game():
        """
        Reset score & code, start new game
        """
        start_select = input(
            '\nTo play again, type ' +
            colored('Y ', 'green') + 'otherwise enter ' +
            colored('N ', 'red') + 'to exit game:\n').lower()
        if start_select == 'y':
            os.system("clear")
            main()

        elif start_select == 'n':
            os.system("clear")
            print(colored("\nThanks for playing. " +
                          "See you next time!!!!\n", "green"))
            exit()

        else:
            print(colored('\nSorry, that is not a valid entry\n', 'red'))


def main():
    """
    Run all program functions and methods to load
    """
    welcome = Welcome()

    # calling the methods in the Welcome class
    welcome.welcome()

    player = Player()

    codegen = Codegen()

    attempts = Attempts()

    newgame = Newgame()

    # calling the methods in the Player class
    player.get_player_name()
    player.game_control()

    # calling the methods in the Codegen class
    codegen.create_comp_list()

    # calling the methods in the Attempts class
    attempts.player_attempts()

    # calling the methods in the Newgame class
    newgame.start_new_game()


if __name__ == '__main__':
    main()
