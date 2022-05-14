""" Main Game Control """
# import player class
from player import Player

# import player class
from codegenerator import Codegen

# import player class
from attempts import Attempts

# import player class
from game import Welcome

# import player class
from game import Newgame


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
