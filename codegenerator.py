""" Codegen Class sets up Codgen object to generate the ENIGMA code """
# import random to create the random secret code
import random

# import termcolor for adding colour to text
from termcolor import colored

# import pyfiglet for ascii art
from pyfiglet import Figlet

# import newgame class
from game import Newgame

newgame = Newgame()


class Codegen:
    """
    Codegen class to get the user's guess, check for errors
    """

    @staticmethod
    def create_comp_list():
        """
        Create the secret random code
        """
        nums = [i+1 for i in range(8)]
        num_list = []

        for i in range(4):
            choice = random.choice(nums)
            while choice in num_list:
                choice = random.choice(nums)
            num_list.append(choice)

        return num_list

    @staticmethod
    def get_guess():
        """
        Get the user's guess, check for errors
        """
        while True:
            # issue default to catch errors in player guess
            num_issue = False
            unique_issue = False
            len_issue = False

            guess = input("Enter your guess (4 unique numbers " +
                          "between 1 and 8): ")

            for number in guess:
                try:
                    if int(number) < 1 or int(number) > 8:
                        num_issue = True

                except ValueError:
                    num_issue = True

            if num_issue:
                print(colored("\nYou can only use numbers " +
                              "1-8 as guesses!\n", "red"))
            else:
                for number in guess:
                    if guess.count(number) > 1:
                        unique_issue = True
                if unique_issue:
                    print(colored("\nYou can only use each " +
                                  "number once!\n", "red"))
                else:
                    if len(guess) != 4:
                        len_issue = True
                    if len_issue:
                        print(colored("\nYour guess must consist " +
                                      "of only 4 numbers!\n", "red"))
                    else:
                        guess_list = list(guess)
                        for i in range(4):
                            guess_list[i] = int(guess_list[i])
                        return guess_list

    def check_values(self, enigma, user):
        """
        Check the players guess values against the ENIGMA code
        """
        return_list = []
        return_list_green = []
        return_list_yellow = []
        return_list_red = []

        for i in range(4):
            if user[i] in enigma:
                if user[i] != enigma[i]:
                    return_list_yellow.append(colored("YELLOW", "yellow"))

        for i in range(4):
            if user[i] in enigma:
                if user[i] == enigma[i]:
                    return_list_green.append(colored("GREEN", "green"))
            else:
                return_list_red.append(colored("RED", "red"))

        # join both lists for printing colour hints with termcolor
        return_list = (
            ' '.join(str(item) for item in return_list_green)) + (' ') + (
                ' '.join(str(item) for item in return_list_yellow)) + (' ') + (
                ' '.join(str(item) for item in return_list_red))
        print("\nENIGMA Hint: " + return_list)
        return self.check_win(return_list)

    def check_win(self, response_list):
        """
        Check if player guesess match ENIGMA code and output win message
        """
        # code to validate player guess against ENIGMA code
        if response_list.split() == ['\x1b[32mGREEN\x1b[0m',
                                     '\x1b[32mGREEN\x1b[0m',
                                     '\x1b[32mGREEN\x1b[0m',
                                     '\x1b[32mGREEN\x1b[0m']:
            win_message = Figlet(font='banner3-D')
            print("\n-----------------\n")
            print(colored(win_message.renderText('YOU WON'), 'green'))
            print("-----------------\n")
            newgame.start_new_game()
            return True
