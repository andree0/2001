from random import choice as c
from dices import choose_dice as cd

DICES_TO_CHOOSE = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']

HTML_START = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
<title>THE 2001 GAME</title>
</head>
<body>
<h1>Start game</h1>
    <form action="" method="POST">
        <input type="hidden" name="gamer_1" value={}>
        <input type="hidden" name="gamer_2" value={}>
        <label for="dice_1">Choose the first dice:</label>
        <select name="dice_1" id="dice_1">
            <option value="D3">D3</option>
            <option value="D4">D4</option>
            <option value="D6">D6</option>
            <option value="D8">D8</option>
            <option value="D10">D10</option>
            <option value="D12">D12</option>
            <option value="D20">D20</option>
            <option value="D100">D100</option>
        </select>
        <label for="dice_2">Choose the second dice:</label>
        <select name="dice_2" id="dice_2">
            <option value="D3">D3</option>
            <option value="D4">D4</option>
            <option value="D6">D6</option>
            <option value="D8">D8</option>
            <option value="D10">D10</option>
            <option value="D12">D12</option>
            <option value="D20">D20</option>
            <option value="D100">D100</option>
        </select>
        <input type="submit" value="roll the dices">
    </form>
</body>
</html>
'''

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
<title>THE 2001 GAME</title>
</head>
<body>
<h1>Your turn</h1>
    <form action="" method="POST">
        <input type="hidden" name="gamer_1" value={}>
        <input type="hidden" name="gamer_2" value={}>
        <label for="dice_1">Choose the first dice:</label>
        <select name="dice_1" id="dice_1">
            <option value="D3">D3</option>
            <option value="D4">D4</option>
            <option value="D6">D6</option>
            <option value="D8">D8</option>
            <option value="D10">D10</option>
            <option value="D12">D12</option>
            <option value="D20">D20</option>
            <option value="D100">D100</option>
        </select>
        <label for="dice_2">Choose the second dice:</label>
        <select name="dice_2" id="dice_2">
            <option value="D3">D3</option>
            <option value="D4">D4</option>
            <option value="D6">D6</option>
            <option value="D8">D8</option>
            <option value="D10">D10</option>
            <option value="D12">D12</option>
            <option value="D20">D20</option>
            <option value="D100">D100</option>
        </select>
        <input type="submit" value="roll the dices">
    </form>
</body>
</html>
'''

HTML_WIN = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
<title>THE 2001 GAME</title>
</head>
<body>
<h1> {} </h1>
<p> Result </p>
<p> {} : {} </p>
</body>
</html>
'''


def game_2001():
    """
    THE 2001 GAME
    """
    print("""
                    THE 2001 GAME
    """)
    gamer_1 = 0
    gamer_2 = 0
    while True:
        first_roll_gamer_1 = cd(input("Choose the first dice:  "))
        if first_roll_gamer_1 is None:
            print("Wrong input")
        elif first_roll_gamer_1 is False:
            print("This dice does not exist")
        else:
            break

    while True:
        second_roll_gamer_1 = cd(input("Choose the second dice:  "))
        if second_roll_gamer_1 is None:
            print("Wrong input")
        elif second_roll_gamer_1 is False:
            print("This dice does not exist")
        else:
            break

    input("Press ENTER to roll dices")
    gamer_1 += first_roll_gamer_1 + second_roll_gamer_1

    first_roll_gamer_2 = cd(c(DICES_TO_CHOOSE))
    second_roll_gamer_2 = cd(c(DICES_TO_CHOOSE))

    gamer_2 += first_roll_gamer_2 + second_roll_gamer_2

    while gamer_1 < 2001 and gamer_2 < 2001:
        print(f'''
            Result gamer_1: {gamer_1}
            Result gamer_2: {gamer_2}
            ''')
        while True:
            third_roll_gamer_1 = cd(input("Choose the first dice:  "))
            if third_roll_gamer_1 is None:
                print("Wrong input")
            elif third_roll_gamer_1 is False:
                print("This dice does not exist")
            else:
                break

        while True:
            fourth_roll_gamer_1 = cd(input("Choose the second dice:  "))
            if fourth_roll_gamer_1 is None:
                print("Wrong input")
            elif fourth_roll_gamer_1 is False:
                print("This dice does not exist")
            else:
                break

        input("Press ENTER to roll dices")

        roll_gamer_1 = third_roll_gamer_1 + fourth_roll_gamer_1

        first_roll_gamer_2 = cd(c(DICES_TO_CHOOSE))
        second_roll_gamer_2 = cd(c(DICES_TO_CHOOSE))

        roll_gamer_2 = first_roll_gamer_2 + second_roll_gamer_2

        if roll_gamer_1 == 7:
            gamer_1 //= 7
        elif roll_gamer_1 == 11:
            gamer_1 *= 11
        else:
            gamer_1 += roll_gamer_1

        if roll_gamer_2 == 7:
            gamer_2 //= 7
        elif roll_gamer_2 == 11:
            gamer_2 *= 11
        else:
            gamer_2 += roll_gamer_1

    print(f"{gamer_1} to {gamer_2}")
    if gamer_1 > gamer_2:
        print('Win gamer_1')
    else:
        print('Win gamer_2')


game_2001()
