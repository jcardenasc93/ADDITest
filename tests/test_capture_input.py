""" Unit testing for input capturing """

from unittest import main
from unittest import TestCase
from unittest.mock import patch

from services.capture_input import InputCapturer


class TestInputCapture(TestCase):
    """ Defines the test case for input capture """

    def setUp(self):
        self._STR = "str"
        self._INT = "int"
        self._FLOAT = "float"

    @patch.object(InputCapturer, 'get_input')
    def test_str_input(self, mock_input):
        """ String input test case """
        mock_input.return_value = 'A string'
        str_capturer = InputCapturer(self._STR)
        str_capturer.capture_input('Enter a string: ')
        self.assertEqual(mock_input.return_value, str_capturer.value)
        self.assertIsInstance(str_capturer.value, str)

    @patch.object(InputCapturer, 'get_input')
    def test_int_input(self, mock_input):
        """ Integer input test case """
        data_type = int
        mock_input.return_value = '12'
        int_capturer = InputCapturer(self._INT)
        int_capturer.capture_input('Enter an integer: ')
        self.assertEqual(data_type(mock_input.return_value), int_capturer.value)
        self.assertIsInstance(int_capturer.value, int)

    @patch.object(InputCapturer, 'get_input')
    def test_float_input(self, mock_input):
        """ Float input test case """
        data_type = float
        mock_input.return_value = '12.5'
        float_capturer = InputCapturer(self._FLOAT)
        float_capturer.capture_input('Enter a float: ')
        self.assertEqual(data_type(mock_input.return_value),
                         float_capturer.value)
        self.assertIsInstance(float_capturer.value, float)
