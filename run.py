""" Main Game Control """
# import player class
from player import Player

# import codegenerator class
from codegenerator import Codegen

# import attempts class
from attempts import Attempts

# import welcome class
from game import Welcome

# import newgame class
from game import Newgame


def main():
    """
    Run all program functions and methods to load game
    """
    welcome = Welcome()

    # calling the Welcome class
    welcome.welcome()

    # calling the Player class
    player = Player()

    # calling the Codegen class
    codegen = Codegen()

    # calling the Attempts class
    attempts = Attempts()

    # calling the Newgame class
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
