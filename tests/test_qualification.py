""" Unit testing for the internal qualification system """

from unittest import main
from unittest import TestCase
from unittest.mock import patch

from services.qualification_system import QualificationSystem


class TestQualificationSystem(TestCase):
    """ Defines the test case for the qualification system """

    def setUp(self):
        min_points = 0
        max_points = 100
        min_score = 60
        self._qualification = QualificationSystem(min_points, max_points,
                                                  min_score)

    @patch.object(QualificationSystem, 'get_random_score')
    def test_success_score_evaluation(self, mock_random_score):
        """ Test case for the success score evaluation method """
        mock_random_score.return_value = 80
        self.assertTrue(self._qualification.score_evaluation())

    @patch.object(QualificationSystem, 'get_random_score')
    def test_fail_score_evaluation(self, mock_random_score):
        """ Test case for the success score evaluation method """
        mock_random_score.return_value = 10
        self.assertFalse(self._qualification.score_evaluation())
