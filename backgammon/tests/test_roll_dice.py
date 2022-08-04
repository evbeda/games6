import unittest
from ..game.dices import roll_dices


class Roll_dices_test(unittest.TestCase):

    def setUp(self):
        self.result = roll_dices()
        self.options = [1, 2, 3, 4, 5, 6]

    def test_roll_dices_numbers_type(self):
        self.assertEqual(int, type(self.result[0]))
        self.assertEqual(int, type(self.result[1]))

    def test_roll_dices_number_interval(self):
        self.assertIn(self.result[0], self.options)
        self.assertIn(self.result[1], self.options)
