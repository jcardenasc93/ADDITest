""" Unit testing for the random integer generator method """
from unittest import main
from unittest import TestCase

from utils.random_integers import get_random_with_range


class TestIntegerGenerator(TestCase):
    """ Defines the test case for the random
    integer generator
    """

    def setUp(self):
        self._min = 7
        self._max = 100

    def test_random_integer(self):
        """ Test case for random integer generator
        in a given range
        """
        rand_int = get_random_with_range(self._min, self._max)
        self.assertTrue(self._min <= rand_int <= self._max)
