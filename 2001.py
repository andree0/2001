from dices import roll_the_dice as r


def game_2001():
    """
    2001 game
    :return:
    """
    print("""
                    THE 2001 GAME
    """)
    gamer_1 = 0
    gamer_2 = 0
    input("Press ENTER to roll dice")
    gamer_1 += r('2D6')
    gamer_2 += r('2D6')
    while gamer_1 < 2001 and gamer_2 < 2001:
        print(f'''
            Result gamer_1: {gamer_1}
            Result gamer_2: {gamer_2}
            ''')
        input("Press ENTER to roll dice")
        roll_gamer_1 = r('2D6')
        roll_gamer_2 = r('2D6')
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
