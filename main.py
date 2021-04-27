""" Main project module """
from services.capture_input import InputCapturer

__author__ = 'Juan Camilo Cardenas'
__version__ = '0.1.0'


def main():
    """ Entry point """
    first_name = InputCapturer("str").capture_input("Enter first name: ")
    last_name = InputCapturer("str").capture_input("Enter last name: ")
    email = InputCapturer("str").capture_input("Enter email: ")
    age = InputCapturer("int").capture_input("Enter age: ")


if __name__ == '__main__':
    main()
