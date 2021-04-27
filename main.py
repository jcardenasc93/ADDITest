""" Main project module """
from services.capture_input import InputCapturer
from services.external_mocks import RequestMocker
from utils.run_parallel import ParallelProcessing

from threading import Thread
import time

__author__ = 'Juan Camilo Cardenas'
__version__ = '0.1.0'


def main():
    """ Entry point """
    first_name = InputCapturer('str').capture_input('Enter first name: ')
    last_name = InputCapturer('str').capture_input('Enter last name: ')
    email = InputCapturer('str').capture_input('Enter email: ')
    age = InputCapturer('int').capture_input('Enter age: ')
    dni = InputCapturer('str').capture_input('Enter national ID number: ')

    # First external call
    # user_data_validation = RequestMocker.mock_external_request('http://nationalid.net')
    id_validation_url = 'http://nationalid.net'
    judicial_validation_url = 'http://wejudgeyou.net'

    id_validation_request = RequestMocker(id_validation_url)
    judicial_validation_request = RequestMocker(judicial_validation_url)

    parallel_runner = ParallelProcessing(
        id_validation_request.mock_external_request,
        judicial_validation_request.mock_external_request)

    parallel_runner.run_tasks_in_parallel()

    print(id_validation_request.response, judicial_validation_request.response)


if __name__ == '__main__':
    main()
