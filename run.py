""" ENIGMA Game import packages to add to program """
# import os to help clear terminal
import os

# import random module
import random

# import termcolor for adding colour to text
from termcolor import colored

# import pyfiglet for ascii art
from pyfiglet import Figlet

# import player class
from player import Player


def clear_game():
    """
    Clear screen to enable new game play
    """
    os.system("clear")


def secret_code(max_range):
    """ Generate random 4 number code """
    secret_code = []
    for _ in range(4):
        secret_code.append(random.randint(1, max_range))
    return secret_code


enigma_code = secret_code(10)
print(enigma_code)
heading = Figlet(font='banner3-D')
print(colored(heading.renderText('ENIGMA'), 'red'))


def welcome():
    """
    ENIGMA Title & welcome message
    """
    sub_heading = Figlet(font='digital')
    print(colored(sub_heading.renderText('Can you crack the code'), 'green'))
    print("Guess all 4 numbers to crack the ENIGMA code!\n")


def main():
    """
    Run all program functions and methods
    """
    welcome()

    player = Player()

    # calling the methods in the Player class
    player.get_player_name()
    player.game_control()

    # Variable to store the correct guesses and attempts
    correct = 0
    attempts = 0

    # Variables to store the players guesses
    while correct < 4:
        attempt1 = int(input('Please guess the 1st number: '))
        attempt2 = int(input('Please guess the 2nd number: '))
        attempt3 = int(input('Please guess the 3rd number: '))
        attempt4 = int(input('Please guess the 4th number: '))
        attempts += 1

        player_guesses = (str(attempt1) + ' ' + str(attempt2) + ' ' +
                          str(attempt3) + ' ' + str(attempt4))

        if attempt1 == enigma_code[0]:
            correct += 1
        if attempt2 == enigma_code[1]:
            correct += 1
        if attempt3 == enigma_code[2]:
            correct += 1
        if attempt4 == enigma_code[3]:
            correct += 1

        if correct < 4 and correct > 1:
            print(colored('\nTry again you cracked ' +
                  str(correct) + ' numbers correctly\n', 'red'))
            print('You guessed ' + str(player_guesses) + ' \n')
            correct = 0
            continue
        elif correct == 1:
            print(colored("\nLet's Get Cracking!\n", 'green'))
            print(colored('\nTry again you cracked ' +
                  str(correct) + ' number correctly\n', 'red'))
            print('You guessed ' + str(player_guesses) + ' \n')
            correct = 0
            continue
        else:
            if correct > 1:
                win_heading = Figlet(font='banner3-D')
                print(colored(win_heading.renderText('\nYOU WON'), 'green'))
                print('\nCongratulations you cracked the Enigma code!!' +
                      ' You did it in ' + str(attempts) + ' tries.\n')
                print('The Enigma Code is ' + str(player_guesses) + ' \n')
            elif correct == 1:
                win_heading = Figlet(font='banner3-D')
                print(colored(win_heading.renderText('\nYOU WON'), 'green'))
                print('\nCongratulations you cracked the Enigma code!!' +
                      ' You did it in ' + str(attempts) + ' try.\n')
                print('The Enigma Code is ' + str(player_guesses) + ' \n')


if __name__ == '__main__':
    main()
