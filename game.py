""" Game and Welcome Class sets up module """
from time import sleep
import sys
import os
from termcolor import colored
from pyfiglet import Figlet

# import Codegen class from codegenerator
from codegenerator import Codegen

code = Codegen()


class Game:
    """
    Player class get the players input for name,
    option to view help instructions.
    Validate players quess inputs
    and return vaildation
    """

    def get_player_guess(self):
        """
        Get the players guess, check for errors
        """
        while True:
            # issue default to catch errors in player guess
            number_issue = False
            unique_issue = False
            length_issue = False

            player_guess = input("Enter your guess: ")

            for number in player_guess:
                try:
                    if int(number) < 1 or int(number) > 8:
                        number_issue = True

                except ValueError:
                    number_issue = True

            if number_issue:
                print(colored("\nYou can only use numbers " +
                              "1-8 as guesses!\n", "red"))
            else:
                for number in player_guess:
                    if player_guess.count(number) > 1:
                        unique_issue = True
                if unique_issue:
                    print(colored("\nYou can only use each " +
                                  "number once!\n", "red"))
                else:
                    if len(player_guess) != 4:
                        length_issue = True
                    if length_issue:
                        print(colored("\nYour guess can only consist " +
                                      "of only 4 numbers!\n", "red"))
                    else:
                        guess_list = list(player_guess)
                        for i in range(4):
                            guess_list[i] = int(guess_list[i])
                        print('\nYou guessed: ' + player_guess)
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
            self.start_new_game()
            return True

    def player_attempts(self):
        """
        Keep track of the player attempts display game lost message
        """
        attempts = 10
        enigma_list = code.create_enigma_list()
        while True:
            if self.check_values(enigma_list, self.get_player_guess()) is True:
                break
            else:
                attempts -= 1
                print("\nAttempts left:", colored(attempts, 'red'))
                print("----------\n")
                if attempts == 0:
                    # output lose message if attempts reach 0
                    lose_message = Figlet(font='banner3-D', justify="center")
                    print(colored(lose_message.renderText('YOU LOSE'), 'red'))
                    print("\nYou are out of attempts! " +
                          colored("GAME OVER.", "red"))
                    player_list = ""
                    for i in range(4):
                        player_list += str(enigma_list[i])
                    print("\nThe " + colored("ENIGMA ", "red") +
                          "code was: " + player_list)
                    self.start_new_game()

                    break

    def start_new_game(self):
        """
        Reset score & code, start new game
        """
        start_select = input(
            '\nTo play again, type ' +
            colored('Y ', 'green') + 'otherwise enter ' +
            colored('N ', 'red') + 'to exit game:\n').lower()
        if start_select == 'y':
            os.system("clear")
            os.system('python run.py')

        elif start_select == 'n':
            os.system("clear")
            bye_message = Figlet(font='digital', justify="center")
            print(colored(bye_message.renderText(
             '\nGoodbye thanks for playing'), 'green'))
            exit()

        else:
            print(colored('\nSorry, that is not a valid entry\n', 'red'))


class Welcome:
    """
    Welcome Message at start of game
    """
    @staticmethod
    def welcome():
        """
        ENIGMA Title & welcome message
        """
        heading = Figlet(font='banner3-D', justify="center")
        print(heading.renderText('ENIGMA'))

        sub_heading = Figlet(font='digital', justify="center")
        print(colored(sub_heading.renderText(
             'Can you crack the code'), 'green'))
        welcome_text = ('Guess all 4 numbers to crack the' +
                        (colored(' ENIGMA ', 'red') +
                         'code!\n'))
        for char in welcome_text:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
