""" Main Game Control """
# import Player class
from player import Player

# import Codegen class
from codegenerator import Codegen

# import Welcome class
from game import Welcome

# import Game class
from game import Game


def main():
    """
    Run all program functions and methods to load game
    """
    # calling the Welcome class
    welcome = Welcome()

    # calling the Player class
    player = Player()

    # calling the Codegen class
    codegen = Codegen()

    # calling the Game class
    game = Game()

    # calling the method in the Welcome class
    welcome.welcome()

    # calling the methods in the Player class
    player.get_player_name()
    player.enigma_game_control()

    # calling the method in the Codegen class
    codegen.create_enigma_list()

    # calling the methods in the Game class
    game.player_attempts()
    game.start_new_game()


if __name__ == '__main__':
    main()
