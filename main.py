""" Main project module """
from services.capture_input import InputCapturer
from services.external_mocks import RequestMocker
from services.qualification_system import QualificationSystem
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

    # Set fake urls
    id_validation_url = 'http://nationalid.net'
    judicial_validation_url = 'http://wejudgeyou.net'

    # Defines the required mockers
    id_validation_request = RequestMocker(id_validation_url)
    judicial_validation_request = RequestMocker(judicial_validation_url)

    # Run tasks in parallel
    parallel_runner = ParallelProcessing(
        id_validation_request.mock_external_request,
        judicial_validation_request.mock_external_request)

    parallel_runner.run_tasks_in_parallel()

    if judicial_validation_request.response == 'successful' and id_validation_request.response == 'successful':
        qualifier = QualificationSystem(0, 100)
        if qualifier.score_evaluation():
            print("Person with DNI {} is now a prospect".format(dni))
    else:
        print("Sorry, the person doesn't meet the requirements")


if __name__ == '__main__':
    main()
