""" Player Class sets up player object """
# import os to help clear terminal
import os

# import re to search blank spaces in username
import re

# import sys for type style
import sys

# import sleep to enable a delay
from time import sleep

# import pyfiglet for ascii art
from pyfiglet import Figlet

# import termcolor for adding colour to text
from termcolor import colored


class Player:
    """
    Player class get the players input for name,
    option to view help instructions.
    Validate players quess inputs
    and return vaildation
    """

    def get_player_name(self):
        """
        Get username input from player
        """
        while True:
            username_data = input("\nEnter your name here to start play:\n")

            if self.validate_data(username_data):
                print(colored('\nWelcome ' +
                              f'{username_data.upper()}\n', 'green'))
                in_ten_or_less_text = ('Can you crack the' +
                                       (colored(' ENIGMA ', 'red') +
                                        'code in 10 or less guesses!'))
                for char in in_ten_or_less_text:
                    sleep(0.1)
                    sys.stdout.write(char)
                    sys.stdout.flush()

                print("\n-----------------\n")

                break

    def validate_data(self, username):
        """
        Validates the username input
        """
        # If input empty and enter hit return error,
        # or if only numbers entered return error
        # otherwise accept all characters for codename
        try:
            if not username or re.search(r"^\s*$", username):
                raise ValueError(colored('Sorry username ' +
                                         'cannot be empty', 'red'))
            elif username.isdigit():
                raise ValueError(colored('Sorry username cannot be ' +
                                         'just a number', 'red'))

        except ValueError as error:
            print(colored(f'Try again! {error}', 'red'))
            return False

        return True

    def game_control(self):
        """
        Give the player the option to display help
        or intructions
        """
        control_select = input(
            '\nTo see game help enter ' +
            colored('H ', 'red') +
            'otherwise enter ' +
            colored('P ', 'green') +
            'to Play game:\n').lower()

        if control_select == 'h':
            print("-----------------------\n")
            print(colored('\nHOW TO PLAY ENIGMA:\n', 'yellow'))
            print("-----------------------\n")
            print('You have ' + colored('10', 'yellow') + ' attempts ' +
                  'to guess the ' + colored('ENIGMA ', 'red') + 'code\n')
            print('The ' + colored('ENIGMA ', 'red') + 'code is ' +
                  colored('4 ', 'yellow') +
                  'random numbers between 1-6')
            print('\nYour guess must be ' + colored('4 ', 'yellow') +
                  'digits, and ' + 'you can only use the same digit once!')
            print('\nAll digits in the code must be between 1 and 6')
            print("\nThe guess format works in two ways: '1234' or '1 2 3 4'")
            print("-----------------------")
            print('\nAfter each guess, you will get ' +
                  'four responses in random order:\n')
            print(colored("GREEN: ", "green") +
                  "One of your numbers is correct " +
                  "& it's in the correct location!\n")
            print(colored("YELLOW: ", "yellow") +
                  "One of your numbers is correct, " +
                  "but it's not in the correct location!\n")
            print(colored('RED: ', 'red') +
                  'One of your numbers is not in the ' +
                  colored('ENIGMA ', 'red') + 'code')
            print("-----------------------")
            control_select = input(
                '\nTo Play game enter ' +
                colored('P ', 'green') +
                'otherwise enter ' +
                colored('X ', 'red') +
                'to Exit game:\n').lower()

            if control_select == "p":
                os.system("clear")
                heading = Figlet(font='banner3-D')
                print(colored(heading.renderText('ENIGMA'), 'red'))
                getcracking_text = (colored("\nLet's Get " +
                                            "Cracking!\n", "green"))
                for char in getcracking_text:
                    sleep(0.1)
                    sys.stdout.write(char)
                    sys.stdout.flush()
            elif control_select == 'x':
                print('Sorry to see you go come back antother time!!!')
                exit()
            else:
                print(colored('Sorry, that is not a valid ' +
                              'entry only\n', 'red'))
                self.game_control()

            # getcracking_text = (colored("\nLet's Get Cracking!\n", "green"))
            # for char in getcracking_text:
            #     sleep(0.1)
            #     sys.stdout.write(char)
            #     sys.stdout.flush()

        elif control_select == "p":
            os.system("clear")
            heading = Figlet(font='banner3-D')
            print(colored(heading.renderText('ENIGMA'), 'red'))
            getcracking_text = (colored("\nLet's Get Cracking!\n", "green"))
            for char in getcracking_text:
                sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()

        else:
            print(colored('Sorry, that is not a valid entry only ' +
                          'H or P accepted\n', 'red'))
            self.game_control()
