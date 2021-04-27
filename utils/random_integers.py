""" Defines a method to get a random integer """

import random

def get_random_with_range(min_num: int, max_num: int):
    """ This method returns a random integer between the specified
    range
    """
    return random.randint(min_num, max_num)

