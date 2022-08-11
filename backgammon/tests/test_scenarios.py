from backgammon.game.constants import MESSAGE_FP, MESSAGE_SP

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

next_turn_resume_true = {
    "board": "board",
    "dices": [1, 2],
    "points": {"BLACK": 3, "WHITE": 2},
    "number_of_turns": 20,
    "piece_captured": {"BLACK": 1, "WHITE": 0}
}

next_turn_resume_false_B = {
    "result": "BLACK WINS",
    "point": {"BLACK": 15, "WHITE": 2}
}

next_turn_resume_false_W = {
    "result": "WHITE WINS",
    "point": {"BLACK": 10, "WHITE": 15}
}

next_turn_resume_false_TIE = {
    "result": "TIE",
    "point": {"BLACK": 15, "WHITE": 15}
}

next_turn_active = f"{next_turn_resume_true} \n {MESSAGE_FP} {MESSAGE_SP}"

next_turn_message_B = f"{next_turn_resume_false_B} \n GAME OVER"
next_turn_message_W = f"{next_turn_resume_false_W} \n GAME OVER"
next_turn_message_TIE = f"{next_turn_resume_false_TIE} \n GAME OVER"
