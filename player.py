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
            print(colored("\nWelcome " + f"{username_data}"), 'green')
