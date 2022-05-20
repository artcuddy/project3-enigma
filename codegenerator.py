""" Codegen Class sets up Codegen object to generate the ENIGMA code """
import random


class Codegen:
    """
    Codegen class generate the random ENIGMA Code
    """

    @staticmethod
    def create_enigma_list():
        """
        Create the randon ENIGMA code
        """
        nums = [i+1 for i in range(8)]
        num_list = []

        for i in range(4):
            choice = random.choice(nums)
            while choice in num_list:
                choice = random.choice(nums)
            num_list.append(choice)

        return num_list
