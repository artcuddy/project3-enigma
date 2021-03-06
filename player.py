""" Player Class sets up player object """
import os
import re
import sys
from time import sleep
from pyfiglet import Figlet
from termcolor import colored


class Player:
    """
    Player class get the players input for name,
    option to view game help instructions.
    Validate players quess inputs
    and return vaildation
    """

    def get_player_name(self):
        """
        Get username input from player
        """
        while True:
            playername = input("\nEnter your name here to start play:\n")

            if self.validate_data(playername):
                print(colored('\nWelcome ' +
                              f'{playername.upper()}\n', 'green'))
                in_ten_or_less_text = ('Can you crack the' +
                                       (colored(' ENIGMA ', 'red') +
                                        'code in 10 or less guesses???'))
                for char in in_ten_or_less_text:
                    sleep(0.1)
                    sys.stdout.write(char)
                    sys.stdout.flush()

                print("\n-----------------\n")

                break

    def validate_data(self, username):
        """
        Validates the username input
        If input empty and enter hit return error,
        or if only numbers entered return error
        otherwise accept all characters for codename

        Args:
            param1: self.
            param2: username.

        Returns:
            True: if the username vaildates.
        """
        try:
            if not username or re.search(r"^\s*$", username):
                raise ValueError(colored('Sorry username ' +
                                         'cannot be blank', 'red'))
            elif username.isdigit():
                raise ValueError(colored('Sorry username cannot be ' +
                                         'just a number', 'red'))

        except ValueError as error:
            print(colored(f'Try again! {error}', 'red'))
            return False

        return True

    def enigma_game_control(self):
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
        # Show help screen if h entered
        if control_select == 'h':
            os.system("clear")
            helpscreen()
            help_select = input(
                '\nTo Play game enter ' +
                colored('P ', 'green') +
                'otherwise enter ' +
                colored('X ', 'red') +
                'to Exit help:\n').lower()
            # Start game if p is entered
            if help_select == "p":
                os.system("clear")
                heading = Figlet(font='banner3-D', justify="center")
                print(heading.renderText('ENIGMA'))
                getcracking_text = (colored("Let's Get " +
                                            "Cracking!\n", "green"))
                for char in getcracking_text:
                    sleep(0.1)
                    sys.stdout.write(char)
                    sys.stdout.flush()
            # Exit help if x is entered
            elif help_select == 'x':
                os.system("clear")
                self.enigma_game_control()
            else:
                print(colored('Sorry, that is not a valid ' +
                              'entry only P or X accepted\n', 'red'))
                self.enigma_game_control()

        elif control_select == "p":
            os.system("clear")
            heading = Figlet(font='banner3-D', justify="center")
            print(heading.renderText('ENIGMA'))
            getcracking_text = (colored("Let's Get Cracking!\n", "green"))
            for char in getcracking_text:
                sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()

        else:
            print(colored('Sorry, that is not a valid entry only ' +
                          'H or P accepted\n', 'red'))
            self.enigma_game_control()


def helpscreen():
    """
    function to display help screen for intructions
    """
    print("-----------------------\n")
    print(colored('\nHOW TO PLAY ENIGMA:\n', 'yellow'))
    print("-----------------------\n")
    print('You have ' + colored('10', 'yellow') + ' attempts ' +
          'to guess the ' + colored('ENIGMA ', 'red') + 'code\n')
    print('The ' + colored('ENIGMA ', 'red') + 'code is ' +
          colored('4 ', 'yellow') +
          'random numbers between 1-8')
    print('\nYour guess must be ' + colored('4 ', 'yellow') +
          'numbers, and ' + 'you can only use the same number once!')
    print('\nAll numbers in the code must be between 1 and 8')
    print("\nThe guess input format works " +
          "in two ways: '1234' or '1 2 3 4'")
    print("-----------------------")
    print('\nAfter each guess, you will get ' +
          'four responses in random order:\n')
    print(colored("GREEN: ", "green") +
          "1 of your numbers is correct " +
          "& it's in the correct location!\n")
    print(colored("YELLOW: ", "yellow") +
          "1 of your numbers is correct, " +
          "but it's not in the correct location!\n")
    print(colored('RED: ', 'red') +
          '1 of your numbers is not in the ' +
          colored('ENIGMA ', 'red') + 'code at all')
    print(colored('\nMatch all 4 numbers to crack the ', 'green') +
          colored('ENIGMA ', 'red') + colored('code\n', 'green'))
    print("-----------------------")
