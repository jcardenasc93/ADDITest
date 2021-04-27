""" This module allows to capture inputs from CLI """


class InputCapturer:
    """ Class definition to capture user input """

    def __init__(self, data_type: str):
        self._data_type = data_type
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, user_input: str):
        """ This method capure inputs from CLI and transform to
        the defined python type
        """
        try:
            self._value = eval(self._data_type)(user_input)
        except NameError as e:
            print('Not valid python type: {}'.format(e))
        except ValueError:
            print('Invalid value for the specified data type. Expecting: {}'.
                  format(eval(self._data_type)))

    def capture_input(self, user_msg: str):
        """ This method captures input from CLI """
        self.value = input(user_msg)
