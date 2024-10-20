import unittest
from tests.nist.longest_run import longest_run_test

class TestFrequency(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            "11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010",  # NIST example
        ]

    def test_regular_input(self):
        result = longest_run_test(self.test_data[0])
        expected = 0.180598
        self.assertAlmostEqual( result, expected, places = 5 )
