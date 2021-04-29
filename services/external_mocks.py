""" This module allows to mock request to external systems """

import requests
import requests_mock
import random

from utils.latency_simulator import LatencySimulator
from utils.random_integers import get_random_with_range


class RequestMocker:
    """ Class definition to mock external requests """

    def __init__(self, api_url):
        self._api_url = api_url
        self.response = None
        SUCCESSFUL = "successful"
        FAILURE = "failure"
        self.RESPONSES = [SUCCESSFUL, FAILURE]

    def mock_external_request(self):
        """ This method mocks an external request response """
        request_reponse = self.RESPONSES[random.getrandbits(1)]
        with requests_mock.Mocker() as mocker:
            # Set mock response
            mocker.get(self._api_url, text=request_reponse)
            RequestMocker.introduce_latency()
            try:
                requests.get(self._api_url)
            except requests_mock.exceptions.NoMockAddress:
                self.mock_external_request()
        self.response = request_reponse

    @staticmethod
    def introduce_latency():
        """ This function simulates latency in the requests
        based on the genration of a random sleep time
        """
        # Calcs random bytes to sent in the request
        bytes_to_sent = get_random_with_range(1024, 2048)
        # Calcs random bandwith to use for the latency
        bandwidth = get_random_with_range(10, 500)
        latency_simulator = LatencySimulator(bandwidth, bytes_to_sent)
        latency_simulator.apply_latency()
