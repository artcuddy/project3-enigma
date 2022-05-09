""" Main Game Code """
# import random to create the random secret code
import random

# import termcolor for adding colour to text
from termcolor import colored

# import pyfiglet for ascii art
from pyfiglet import Figlet

# import player class
from player import Player


def create_comp_list():
    """
    Create the secret random code
    """
    nums = [i+1 for i in range(7)]
    num_list = []

    for i in range(4):
        choice = random.choice(nums)
        while choice in num_list:
            choice = random.choice(nums)
        num_list.append(choice)

    return num_list


def get_guess():
    """
    Get the user's guess, check for errors
    """
    while True:
        num_issue = False
        unique_issue = False
        len_issue = False
        value_issue = False
        # defaults ^

        guess = input("Enter your guess (4 unique numbers between 1 and 9): ")
        for number in guess:
            try:
                if int(number) < 1 or int(number) > 9:
                    num_issue = True
            except ValueError:
                value_issue = True
        if value_issue:

            guess = guess.split()
            guess_text = ""
            for i in range(4):
                guess[i] = int(guess[i])
                guess_text += str(guess[i])

        if num_issue:
            print("You can only use numbers 1-9 as guesses!")
        else:
            for number in guess:
                if guess.count(number) > 1:
                    unique_issue = True
            if unique_issue:
                print("You can only use each number once!")
            else:
                if len(guess) != 4:
                    len_issue = True
                if len_issue:
                    print("Your guess must consist of 4 numbers!")
                else:
                    guess_list = list(guess)
                    for i in range(4):
                        guess_list[i] = int(guess_list[i])
                    return guess_list


def check_values(comp, user):
    """
    Check the players guess values
    """
    return_list = []
    for i in range(4):
        if user[i] in comp:
            if user[i] != comp[i]:
                return_list.append("YELLOW")
            else:
                return_list.append("GREEN")
        else:
            return_list.append("RED")
    random.shuffle(return_list)
    print(return_list)
    return check_win(return_list)


def check_win(response_list):
    """
    Check if player has won
    """
    if response_list == ["GREEN", "GREEN", "GREEN", "GREEN"]:
        win_message = Figlet(font='banner3-D')
        print(colored(win_message.renderText('\nYOU WON'), 'green'))
        print("\nThe ENIGMA code was: " + player_list)
        start_new_game()
        return True


def main():
    """
    Run all program functions and methods
    """
    welcome()

    player = Player()

    # calling the methods in the Player class
    player.get_player_name()
    player.game_control()

    attempts = 10
    computer_list = create_comp_list()
    while True:
        if check_values(computer_list, get_guess()) is True:
            break
        else:
            attempts -= 1
            print("\nattempts left", attempts)
            print("----------\n")
            if attempts == 0:
                lose_message = Figlet(font='banner3-D')
                print(colored(lose_message.renderText('YOU LOSE'), 'red'))
                print("You are out of attempts! GAME OVER.")
                player_list = ""
                for i in range(4):
                    player_list += str(computer_list[i])
                print("\nThe ENIGMA code was: " + player_list)
                start_new_game()

                break


def start_new_game():
    """
    Reset score & code, start new game
    """
    play_again = input('\nTo play again, type yes ' +
                       'or no and hit enter: ')
    if play_again == 'yes':
        main()
    else:
        exit()


def welcome():
    """
    ENIGMA Title & welcome message
    """
    heading = Figlet(font='banner3-D')
    print(colored(heading.renderText('ENIGMA'), 'red'))

    sub_heading = Figlet(font='digital')
    print(colored(sub_heading.renderText('Can you crack the code'), 'green'))
    print("Guess all 4 numbers to crack the ENIGMA code!\n")


if __name__ == '__main__':
    main()
