import random


def roll_dices():
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    return (dice_one, dice_two)
