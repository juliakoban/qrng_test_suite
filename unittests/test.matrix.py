import unittest
from tests.nist.matrix import binary_matrix_rank_test

class TestFrequency(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            "01011001001010101101",  # NIST example
        ]

    def test_regular_input(self):
        result = binary_matrix_rank_test( self.test_data[0], M = 3, Q = 3 )
        expected = 0.741948
        self.assertAlmostEqual( result, expected, places = 5 )