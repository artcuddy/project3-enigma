""" Player Class sets up player object """
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
            username_data = input("Enter your name here to start play:\n")

            if self.validate_data(username_data):
                print(colored('\nWelcome ' +
                              f'{username_data.upper()}\n', 'green'))
                print('Can you crack the' + (colored(' ENIGMA ', 'red')
                      + 'code in 10 or less guesses!\n'))
                break

    def validate_data(self, username):
        """
        Validates the username input
        """
        # If input empty and enter hit return error,
        # or if only numbers entered return error
        # otherwise accept all characters for codename
        try:
            if len(username) == 0:
                raise ValueError(colored('Input cannot be empty', 'red'))
            elif username.isdigit():
                raise ValueError(colored('Input cannot be ' +
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
            'To see game help enter ' +
            colored('H ', 'red') +
            'otherwise enter ' +
            colored('P ', 'green') +
            'to Play game:\n').lower()

        if control_select == 'h':
            print(colored('\nHOW TO PLAY ENIGMA:\n', 'yellow'))
            print('You have ' + colored('10', 'yellow') + ' attempts ' +
                  'to guess the ENIGMA code\n')
            print('The ENIGMA code is 4 random numbers between 1-9')
            print('\nYour guess must be 4 digits, and ' +
                  'you can only use the same digit once!')
            print('All digits in the code must be between 1 and 9')
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
