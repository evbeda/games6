import unittest
import random
from select_player import select_player
from unittest.mock import patch

class SelectPalyerTest(unittest.TestCase):

    @patch('random.randint', return_value=1)
    def test_player_1(self, patched_randint):
        player = select_player()
        self.assertEqual(player, 1)
        #import pdb; pdb.set_trace()

    @patch('random.randint', return_value=2)
    def test_player_2(self, patched_randint):
        player = select_player()
        self.assertEqual(player, 2)
        #import pdb; pdb.set_trace()

if __name__ == '__main__':
    unittest.main()

