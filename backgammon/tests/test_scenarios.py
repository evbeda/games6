from backgammon.game.constants import (
    MESSAGE_FP,
    MESSAGE_SP,
    WINNER_WHITE,
    WINNER_BLACK,
    TIE,
    BLACK,
    WHITE)

initial_board = [
    [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
    [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 0], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 2]
]

board_1 = [
    [2, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1],
    [0, 0], [0, 3], [0, 0], [0, 0], [1, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 2], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 2]
]
board_2 = [
    [2, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1],
    [0, 0], [0, 3], [0, 0], [0, 0], [1, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 2], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 2]
]
initial_board2 = [
    [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
    [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 0], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 2]
]
board_7 = [
    [2, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1],
    [0, 0], [0, 3], [0, 0], [0, 0], [1, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 2], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 2]
]

board_3 = [
    [2, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1],
    [0, 0], [0, 3], [0, 0], [0, 0], [1, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 2], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 1], [1, 0], [0, 0]
]

board_4 = [
    [2, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1],
    [0, 0], [0, 3], [0, 0], [0, 0], [1, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 2], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 1], [1, 0], [0, 0]
]

board_5 = [
    [0, 0], [1, 0], [0, 0], [0, 1], [0, 0], [0, 1],
    [0, 0], [0, 3], [0, 0], [0, 0], [1, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 2], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 1], [1, 0], [0, 3]
]

board_6 = [
    [2, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1],
    [0, 0], [0, 3], [0, 0], [0, 0], [1, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 2], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 1], [1, 0], [0, 0]
]

board_8 = [
    [2, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1],
    [0, 0], [0, 3], [0, 0], [0, 0], [1, 0], [5, 0],
    [0, 5], [0, 0], [0, 0], [0, 0], [3, 2], [0, 0],
    [5, 0], [0, 0], [0, 0], [0, 1], [1, 0], [0, 0]
]
presented_initial_board = [
    '131415161718 192021222324',
    'B | | | W |   W | | | | B',
    'B | | | W |   W | | | | B',
    'B | | | W |   W | | | | |',
    'B | | | | |   W | | | | |',
    'B | | | | |   W | | | | |',
    '                         ',
    'W | | | | |   B | | | | |',
    'W | | | | |   B | | | | |',
    'W | | | B |   B | | | | |',
    'W | | | B |   B | | | | W',
    'W | | | B |   B | | | | W',
    '1211109 8 7   6 5 4 3 2 1',
]
presented_board7 = [
    '131415161718 192021222324',
    'B | | | W |   W | | B | B',
    'B | | | W |   W | | | | B',
    'B | | | W |   W | | | | |',
    'B | | | | |   W | | | | |',
    'B | | | | |   W | | | | |',
    '                         ',
    'W | | | | |   | | | | | |',
    'W | | | | |   | | | | | |',
    'W | | | B |   | | | | | |',
    'W | | | B |   | | | | | W',
    'W W | | B |   B | B | | W',
    '1211109 8 7   6 5 4 3 2 1',
]

next_turn_resume_true = {
    "dices": [1, 2],
    "move_options": [1, 2, 3],
    "points": {BLACK: 3, WHITE: 2},
    "number_of_turns": 20,
    "piece_captured": {"BLACK": 1, "WHITE": 0}
}

next_turn_resume_false_B = {
    "result": WINNER_BLACK,
    "point": {BLACK: 15, WHITE: 2}
}

next_turn_resume_false_W = {
    "result": WINNER_WHITE,
    "point": {BLACK: 10, WHITE: 15}
}

next_turn_resume_false_TIE = {
    "result": TIE,
    "point": {BLACK: 15, WHITE: 15}
}

message = f"BLACK turn. {next_turn_resume_true} \n {MESSAGE_FP} {MESSAGE_SP}"
next_turn_message_B = f"{next_turn_resume_false_B} \n GAME OVER"
next_turn_message_W = f"{next_turn_resume_false_W} \n GAME OVER"
next_turn_message_TIE = f"{next_turn_resume_false_TIE} \n GAME OVER"
