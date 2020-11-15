from random import choice as c
from dices import choose_dice as cd
from flask import Flask
from flask import request

app = Flask(__name__)

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
        <label>
        <input type="hidden" name="gamer_1" value={}>
        <input type="hidden" name="gamer_2" value={}>
        </label>        
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
        <table
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
        <label>
        <input type="hidden" name="gamer_1" value={}>
        <input type="hidden" name="gamer_2" value={}>
        </label>   
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
        </select> \n
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
<h2> Result </h2>
<p> {} : {} </p>
<input type="submit" name="try_again" value="Try again">
</body>
</html>
'''


@app.route("/", methods=['GET', 'POST'])
def game_2001():
    """
    THE 2001 GAME
    """
    if request.method == 'GET':
        return HTML_START.format(0, 0)
    else:
        gamer_1 = int(request.form["gamer_1"])
        gamer_2 = int(request.form["gamer_2"])
        if gamer_1 == 0 and gamer_2 == 0:
            first_roll_gamer_1 = int(cd(request.form["dice_1"]))
            second_roll_gamer_1 = int(cd(request.form["dice_2"]))

            gamer_1 += first_roll_gamer_1 + second_roll_gamer_1

            first_roll_gamer_2 = int(cd(c(DICES_TO_CHOOSE)))
            second_roll_gamer_2 = int(cd(c(DICES_TO_CHOOSE)))

            gamer_2 += first_roll_gamer_2 + second_roll_gamer_2

            return HTML.format(gamer_1, gamer_2)

        elif request.form["try_again"]:
            return HTML_START.format(0, 0)
        elif gamer_1 > 2001 or gamer_2 > 2001:
            if gamer_1 > gamer_2:
                return HTML_WIN.format("Congratulation, You win !", gamer_1, gamer_2)
            else:
                return HTML_WIN.format("Sorry, You lose :(", gamer_1, gamer_2)
        else:
            third_roll_gamer_1 = int(cd(request.form["dice_1"]))
            fourth_roll_gamer_1 = int(cd(request.form["dice_2"]))

            roll_gamer_1 = third_roll_gamer_1 + fourth_roll_gamer_1

            third_roll_gamer_2 = int(cd(c(DICES_TO_CHOOSE)))
            fourth_roll_gamer_2 = int(cd(c(DICES_TO_CHOOSE)))

            roll_gamer_2 = third_roll_gamer_2 + fourth_roll_gamer_2

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

            return HTML.format(gamer_1, gamer_2)


if __name__ == "__main__":
    app.run(debug=True, port=5800)
