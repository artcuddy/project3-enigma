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
            username_data = input("Enter your codename here to start play:\n")

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
        Give the player the option to disply help
        or intructions 
        """
        control_select = input(
            'To see game help enter ' +
            colored('H ', 'red') +
            'otherwise enter ' +
            colored('P ', 'green') +
            'to Play game:\n').lower()

