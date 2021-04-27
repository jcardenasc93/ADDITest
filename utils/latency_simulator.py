""" This module defines a latency simulator """

import time
from utils.random_integers import get_random_with_range

class LatencySimulator:
    """ Class definition to simulate a request latency simulator """

    def __init__(self, bandwidth: int, bytes_sent: int):
        """ Constructor definition for LatencySimulator object
        Args:
            bandwidth (int): Integer number to specify bandwidth to use
            bytes_sent (int): Integer number to specify the quantity of
                              bytes to be sent
        """
        self._bandwidth = bandwidth
        self._bytes_sent = bytes_sent
        # Get a random latency between 200ms and 2500ms
        self._latency = get_random_with_range(200, 2500)

    def apply_latency(self):
        """ Apply latency based on simple calculations """
        required_time = self._bytes_sent / self._bandwidth
        time.sleep(max(required_time, self._latency)/1000)

