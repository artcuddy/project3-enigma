""" Attempts Class sets up attempts object """

# import termcolor for adding colour to text
from termcolor import colored

# import pyfiglet for ascii art
from pyfiglet import Figlet

# import player class
from codegenerator import Codegen

# import newgame class
from game import Newgame


code = Codegen()

newgame = Newgame()


class Attempts:
    """
    Keep track of the player attempts and check if player has won or lost
    """
    @staticmethod
    def player_attempts():
        """
        Keep track of the player attempts display game lost message
        """
        attempts = 10
        computer_list = code.create_comp_list()
        while True:
            if code.check_values(computer_list, code.get_guess()) is True:
                break
            else:
                attempts -= 1
                print("\nAttempts left", attempts)
                print("----------\n")
                if attempts == 0:
                    # output lose message if attempts reach 0
                    lose_message = Figlet(font='banner3-D', justify="center")
                    print(colored(lose_message.renderText('YOU LOSE'), 'red'))
                    print("\nYou are out of attempts! " +
                          colored("GAME OVER.", "red"))
                    player_list = ""
                    for i in range(4):
                        player_list += str(computer_list[i])
                    print("\nThe " + colored("ENIGMA ", "red") +
                          "code was: " + player_list)
                    newgame.start_new_game()

                    break
