""" This module allows to mock request to external systems """

import requests
import requests_mock
import random

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
            return requests.get(api_url).text


