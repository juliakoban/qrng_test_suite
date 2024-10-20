import unittest
from tests.nist.frequency import frequency_test

class TestFrequency(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000",  # NIST example
            "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"   # all zeros
        ]

    def test_regular_input(self):
        result = frequency_test(self.test_data[0])
        expected = 0.109599 
        self.assertAlmostEqual( result, expected, places = 5 )

    def test_all_zeros(self):
        result   = frequency_test(self.test_data[1])
        expected = 0.0
        self.assertAlmostEqual(result, expected, places = 5)