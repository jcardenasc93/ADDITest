""" Module to handle the qualification system """

from utils.random_integers import get_random_with_range


class QualificationSystem:
    """ Class definition for the random qualification system """

    def __init__(self, min_points: int, max_points: int, min_score: int):
        self._min_points = min_points
        self._max_points = max_points
        self._min_score = min_score

    def get_random_score(self):
        return get_random_with_range(self._min_points, self._max_points)

    def score_evaluation(self):
        return self.get_random_score() > self._min_score
