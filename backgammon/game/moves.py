def new_positon_check(board, position, number):
    orientation = 1 if board[position][0] else -1
    positionFriendArray = 0 if orientation >= 0 else 1
    positionEnemyArray = 1 if orientation >= 0 else 0

    if orientation > 0 and position + number > 24:
        return True

    if orientation < 0 and position - number < 1:
        return True

    if (board[position + (number * orientation)][positionFriendArray] <= 4
            and board[position + (number * orientation)][positionEnemyArray] < 2):
        return True

    return False
