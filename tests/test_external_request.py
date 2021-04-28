""" Unit testing for request mocker """

from unittest import main
from unittest import TestCase

from services.external_mocks import RequestMocker


class TestRequestMock(TestCase):
    """ Defines the test case for the request
    mocker
    """

    def setUp(self):
        api_url = 'http://just-testing.com'
        self._request = RequestMocker(api_url)

    def test_external_request(self):
        """ Test case for external request """
        self._request.mock_external_request()
        # The reponse should be either suceessful or failure
        self.assertIn(self._request.response, self._request.RESPONSES)
