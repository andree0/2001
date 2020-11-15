import re
from random import randint as r

POSSIBLE_DICES = [3, 4, 6, 8, 10, 12, 20, 100]
CODE = r'^(\d*)D(\d+)([+|-]\d+)*$'


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


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))
    print(roll_the_dice("throw 2D6+15"))
    print(roll_the_dice("2D5"))
