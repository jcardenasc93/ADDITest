""" Main project module """
from services.capture_input import InputCapturer
from services.external_mocks import RequestMocker

__author__ = 'Juan Camilo Cardenas'
__version__ = '0.1.0'


def main():
    """ Entry point """
    first_name = InputCapturer('str').capture_input('Enter first name: ')
    last_name = InputCapturer('str').capture_input('Enter last name: ')
    email = InputCapturer('str').capture_input('Enter email: ')
    age = InputCapturer('int').capture_input('Enter age: ')
    dni = InputCapturer('int').capture_input('Enter national ID number: ')

    # First external call
    user_data_validation = RequestMocker.mock_external_request('http://nationalid.net')
    print(user_data_validation)


if __name__ == '__main__':
    main()
