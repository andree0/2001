import re
from random import randint as r
from flask import request
from random import choice as c

DICES_TO_CHOOSE = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
POSSIBLE_DICES = [3, 4, 6, 8, 10, 12, 20, 100]
CODE = r'^(\d*)D(\d+)([+|-]\d+)*$'
DICE_CODE = r'^D(\d+)$'


def roll_the_dice(dice_code):
    """
    This function check input and return result of roll the dice.
    Input must match the pattern 'xDy +/- z',
    otherwise a message will be displayed.
    """
    check_code = re.search(CODE, dice_code)
    if check_code:
        dice = int(check_code.group(2))
        if dice in POSSIBLE_DICES:
            try:
                multiply = int(check_code.group(1))
            except ValueError:
                multiply = 1

            try:
                modifier = int(check_code.group(3))
            except (ValueError, TypeError):
                modifier = 0

            result = 0
            for i in range(multiply):
                result += r(1, dice)

            result += modifier
            return result
        else:
            return "This dice does not exist"
    else:
        return "Wrong input"


def choose_dice(dice_code):
    """
    This function check input and return result of roll the dice.
    Input must match the pattern 'Dy',
    otherwise a message will be displayed.
    """
    check_code = re.search(DICE_CODE, dice_code)
    if check_code:
        dice = int(check_code.group(1))
        roll_result = 0
        if dice in POSSIBLE_DICES:
            roll_result += r(1, dice)

            return roll_result
        else:
            return False
    else:
        return None


def user_roll(a, b):
    third_roll_gamer_1 = int(choose_dice(request.form[a]))
    fourth_roll_gamer_1 = int(choose_dice(request.form[b]))

    roll_gamer_1 = third_roll_gamer_1 + fourth_roll_gamer_1
    return roll_gamer_1


def computer_roll():
    first_roll_gamer_2 = int(choose_dice(c(DICES_TO_CHOOSE)))
    second_roll_gamer_2 = int(choose_dice(c(DICES_TO_CHOOSE)))

    gamer_2 = first_roll_gamer_2 + second_roll_gamer_2
    return gamer_2


def modifier_points(roll, result):
    if roll == 7:
        result //= 7
    elif roll == 11:
        result *= 11
    else:
        result += roll
    return result


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))
    print(roll_the_dice("throw 2D6+15"))
    print(roll_the_dice("2D5"))
