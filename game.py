""" Newgame and Welcome Class sets up attempts object """
# import sleep to enable a delay
from time import sleep

# import sys for type style
import sys

# import os to help clear terminal
import os

# import termcolor for adding colour to text
from termcolor import colored

# import pyfiglet for ascii art
from pyfiglet import Figlet


class Welcome:
    """
    Welcome Message
    """
    @staticmethod
    def welcome():
        """
        ENIGMA Title & welcome message
        """
        heading = Figlet(font='banner3-D')
        print(colored(heading.renderText('ENIGMA'), 'red'))

        sub_heading = Figlet(font='digital')
        print(colored(sub_heading.renderText(
             'Can you crack the code'), 'green'))
        welcome_text = ('Guess all 4 numbers to crack the' +
                        (colored(' ENIGMA ', 'red') +
                         'code!\n'))
        for char in welcome_text:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()


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
            # main()

        elif start_select == 'n':
            os.system("clear")
            print(colored("\nThanks for playing. " +
                          "See you next time!!!!\n", "green"))
            exit()

        else:
            print(colored('\nSorry, that is not a valid entry\n', 'red'))
