""" ENIGMA Game generates the secret code and validates input """
# import random module
import random

# import termcolor for adding colour to text
from termcolor import colored


class Code:
    """
    Secret code class get the players
    input for guessing the code.
    Validate players quess inputs
    and return vaildation
    """

    # Create a four digit random number
    def create_secret_code(self): # Create the secret code
        nums = [i+1 for i in range(7)]
        num_list = []

        for i in range(4):
            choice = random.choice(nums)
            while choice in num_list:
                choice = random.choice(nums)
            num_list.append(choice)

        return num_list

    secret_code = create_secret_code()
    print(secret_code)

