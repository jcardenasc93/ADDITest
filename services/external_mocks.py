""" This module allows to mock request to external systems """

import requests
import requests_mock
import random

from utils.latency_simulator import LatencySimulator
from utils.random_integers import get_random_with_range

class RequestMocker:
    """ Class definition to mock external requests """
    SUCCESSFUL = "successful"
    FAILURE = "failure"
    RESPONSES = [SUCCESSFUL, FAILURE]

    @classmethod
    def mock_external_request(cls, api_url: str):
        """ This method mocks an external request response """
        request_reponse = cls.RESPONSES[random.getrandbits(1)]
        with requests_mock.Mocker() as mocker:
            # Set mock response
            mocker.get(api_url, text=request_reponse)
            RequestMocker.introduce_latency()
            return requests.get(api_url).text

    @staticmethod
    def introduce_latency():
        """ This function simulates latency in the requests
        based on the genration of a random sleep time
        """
        # Calcs random bytes to sent in the request
        bytes_to_sent = get_random_with_range(1024, 2048)
        # Calcs random bandwith to use for the latency
        bandwith = get_random_with_range(10, 500)
        latency_simulator = LatencySimulator(bandwith, bytes_to_sent)
        latency_simulator.apply_latency()



