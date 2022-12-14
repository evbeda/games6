from backgammon.game.backgammon import BackgammonGame
from guess_number_game.guess_number_game import GuessNumberGame
from othello.othello_game import Othello
from wumpus.game import WumpusGame


class Game(object):

    def __init__(self):
        super(Game, self).__init__()
        self.games = [
            GuessNumberGame,
            Othello,
            WumpusGame,
            BackgammonGame
        ]

    def output(self, text):
        print(text)

    def get_input(self, text):
        return input(text)

    def game_inputs(self):
        game_inputs = 'Select Game\n'
        option_number = 0
        for game in self.games:
            game_inputs += '{}: {}\n'.format(
                option_number,
                game.name,
            )
            option_number += 1
        game_inputs += '99: to quit\n'
        return game_inputs

    def get_input_config(self):
        if isinstance(self.active_game.input_args, tuple):
            input_arg_qtys = self.active_game.input_args
            expecting_input_args = ' or '.join(
                str(input_arg_qty)
                for input_arg_qty in self.active_game.input_args
            )
        else:
            input_arg_qtys = (self.active_game.input_args,)
            expecting_input_args = self.active_game.input_args
        return input_arg_qtys, expecting_input_args

    def process_inputs(self, inputs):
        if self.active_game.input_are_ints:
            return [
                int(simple_arg)
                for simple_arg in inputs.split(' ')
            ]
        else:
            return inputs.split(' ')

    def get_turn_input(self, text):
        input_args = ''
        input_arg_qtys, expecting_input_args = self.get_input_config()
        expecting_str = (
            '{} numbers separated with spaces'.format(
                expecting_input_args,
            )
        )
        while True:
            inputs = self.get_input('{} (expecting {})\n'.format(
                text,
                expecting_str,
            ))
            try:
                # ipdb.set_trace()
                input_args = self.process_inputs(inputs)

                if len(input_args) in input_arg_qtys:
                    break
                else:
                    self.output(
                        'Wrong input count, expecting {} values'.format(
                            self.active_game.input_args
                        )
                    )
            except Exception:
                self.output('Wrong input, try again!')
        return input_args

    def select_game(self):
        result = ''
        while not result.isdigit():
            result = self.get_input(self.game_inputs())
        return int(result)

    def play(self):
        while True:
            game_selection = self.select_game()
            if game_selection == 99:
                break
            if game_selection < len(self.games):
                self.active_game = self.games[game_selection]()
                self.play_game()

    def play_game(self):
        try:
            while (
                (
                    hasattr(self.active_game, 'playing') and
                    self.active_game.playing
                ) or (
                    hasattr(self.active_game, 'is_playing') and
                    self.active_game.is_playing
                )
            ):
                self.output(self.active_game.board)
                game_input = self.get_turn_input(
                    self.active_game.next_turn(),
                )
                self.output(self.active_game.play(*game_input))
        except Exception as e:
            self.output('Sorry... {}'.format(e))


if __name__ == '__main__':
    Game().play()
