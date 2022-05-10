""" Player Class sets up player object """
# import re to search blank spaces in username
import re

# import sys for type style
import sys

# import sleep to enable a delay
from time import sleep

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
                inten_or_less_text = ('Can you crack the' +
                                      (colored(' ENIGMA ', 'red') +
                                       'code in 10 or less guesses!'))
                for char in inten_or_less_text:
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
            print(colored('\nHOW TO PLAY ENIGMA:\n', 'yellow'))
            print('You have ' + colored('10', 'yellow') + ' attempts ' +
                  'to guess the ENIGMA code\n')
            print('The ENIGMA code is ' + colored('4 ', 'yellow') +
                  'random numbers between 1-6')
            print('\nYour guess must be ' + colored('4 ', 'yellow') +
                  'digits, and ' + 'you can only use the same digit once!')
            print('All digits in the code must be between 1 and 6')
            print("The guess format works in two ways: '1234' or '1 2 3 4'")
            print('----------')
            print('\nAfter each guess, you will get ' +
                  'four responses in random order:\n')
            print("GREEN: One of your numbers is correct " +
                  "& it's in the correct location!")
            print("YELLOW: One of your numbers is correct, " +
                  "but it's not in the correct location!")
            print('RED: One of your numbers is not in the ENIGMA code')
            print('----------')
            print(colored("\nLet's Get Cracking!\n", 'green'))

        elif control_select == "p":
            print(colored("\nLet's Get Cracking!\n", 'green'))

        else:
            print(colored('Sorry, that is not a valid entry\n', 'red'))
            self.game_control()
