import unittest
from unittest.mock import patch
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

        class OutputCollector(object):
            def __init__(self, *args, **kwargs):
                self.output_collector = []

            def __call__(self, output):
                self.output_collector.append(output)

        self.output_collector = OutputCollector()

    def tearDown(self):
        pass

    @patch('game.Game.get_input', return_value='99')
    def test_quit_game(self, mock_input):
        with patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            [],
        )

    def test_game_selection(self):
        self.assertEqual(
            self.game.game_inputs(),
            'Select Game\n'
            '0: Guess Number Game\n'
            '1: Othello\n'
            '99: to quit\n'
        )

    def test_play_guess_number_game(self):
        with \
                patch('game.Game.get_input', side_effect=['0', '50', '99']), \
                patch('game.Game.output', side_effect=self.output_collector), \
                patch('guess_number_game.guess_number_game.randint', return_value=50):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            ['[]', 'you win'],
        )


if __name__ == "__main__":
    unittest.main()
