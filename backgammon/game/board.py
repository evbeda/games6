def create_board():
    """
    Generated the initial board
    returns a list of lists
    params: none
    """

    return [
        [0, 0],
        [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
        [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
        [0, 5], [0, 0], [0, 0], [0, 0], [0, 0], [3, 0],
        [0, 0], [5, 0], [0, 0], [0, 0], [0, 0], [0, 2]
    ]


def available_pieces(board, side):

    index = 0 if side == "W" else 1

    result = []
    for i in range(len(board)):
        if board[i][index]:
            result.append(i)
    return result
