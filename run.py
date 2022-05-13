""" Main Game Code """
# import os to help clear terminal
import os

# import random to create the random secret code
import random

# import sys for type style
import sys

# import sleep to enable a delay
from time import sleep

# import termcolor for adding colour to text
from termcolor import colored

# import pyfiglet for ascii art
from pyfiglet import Figlet

# import player class
from player import Player


def main():
    """
    Run all program functions and methods to load
    """
    welcome()

    player = Player()

    code = Codegen()

    # calling the methods in the Player class
    player.get_player_name()
    player.game_control()

    # keep track of the player attempts and check if player has won or lost
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
                # output loser message is attempts reach 0
                lose_message = Figlet(font='banner3-D')
                print(colored(lose_message.renderText('YOU LOSE'), 'red'))
                print("\nYou are out of attempts! " +
                      colored("GAME OVER.", "red"))
                player_list = ""
                for i in range(4):
                    player_list += str(computer_list[i])
                print("\nThe " + colored("ENIGMA ", "red") +
                      "code was: " + player_list)
                start_new_game()

                break


class Codegen:
    """
    Codegen class to get the user's guess, check for errors
    """

    @staticmethod
    def create_comp_list():
        """
        Create the secret random code
        """
        nums = [i+1 for i in range(6)]
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
            value_issue = False

            guess = input("Enter your guess (4 unique numbers " +
                          "between 1 and 6): ")

            for number in guess:
                try:
                    if int(number) < 1 or int(number) > 6:
                        num_issue = True

                except ValueError:
                    value_issue = True

            if num_issue:
                print(colored("\nYou can only use numbers " +
                              "1-6 as guesses!\n", "red"))

            if value_issue:
                print(colored("\nYou can only use numbers " +
                              "1-6 as guesses!\n", "red"))

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
                                      "of 4 numbers!\n", "red"))
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
        Check if player guesess match and output win message
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
            start_new_game()
            return True


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
        main()

    elif start_select == 'n':
        os.system("clear")
        print(colored("\nThanks for playing. " +
                      "See you next time!!!!\n", "green"))
        exit()

    else:
        print(colored('\nSorry, that is not a valid entry\n', 'red'))


def welcome():
    """
    ENIGMA Title & welcome message
    """
    heading = Figlet(font='banner3-D')
    print(colored(heading.renderText('ENIGMA'), 'red'))

    sub_heading = Figlet(font='digital')
    print(colored(sub_heading.renderText('Can you crack the code'), 'green'))
    welcome_text = ('Guess all 4 numbers to crack the' +
                    (colored(' ENIGMA ', 'red') +
                     'code!\n'))
    for char in welcome_text:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


if __name__ == '__main__':
    main()
