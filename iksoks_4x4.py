gameboard = [
    ['','','',''],
    ['','','',''],
    ['','','',''],
    ['','','','']
]

turn = 'X'

def print_gameboard(gameboard):
    print(gameboard[0])
    print(gameboard[1])
    print(gameboard[2])
    print(gameboard[3])

def winner_exists(gameboard):
    if gameboard[0][0] == gameboard[0][1] == gameboard[0][2] == gameboard[0][3] != '' or \
        gameboard[1][0] == gameboard[1][1] == gameboard[1][2] == gameboard[1][3] != '' or \
            gameboard[2][0] == gameboard[2][1] == gameboard[2][2] == gameboard[2][3] != '' or \
                gameboard[3][0] == gameboard[3][1] == gameboard[3][2] == gameboard[3][3] != '' or \
                    gameboard[0][0] == gameboard[1][0] == gameboard[2][0] == gameboard[3][0] != '' or \
                        gameboard[0][1] == gameboard[1][1] == gameboard[2][1] == gameboard[3][1] != '' or \
                            gameboard[0][2] == gameboard[1][2] == gameboard[2][2] == gameboard[3][2] != '' or \
                                gameboard[0][3] == gameboard[1][3] == gameboard[2][3] == gameboard[3][3] != '' or \
                                    gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == gameboard[3][3] != '' or \
                                        gameboard[0][3] == gameboard[1][2] == gameboard[2][1] == gameboard[3][0] != '':
                                    
        return True
    else:
        return False

turn_counter = 0

game_end = False
print_gameboard(gameboard)
while not game_end:
    print('Igrac',turn,'je na potezu, unesite koordinate')

    x = int(input())
    y = int(input())

    while (x>3 and y>3) or gameboard[x][y] != '':
        print('Unos je pogresan - polje je zauzeto il ste unijeli nevalidno polje.')
        x = int(input())
        y = int(input())

    gameboard[x][y] = turn
    turn_counter += 1
    if winner_exists(gameboard):
        print(turn,'is the winner!!!')
        print_gameboard(gameboard)
        gameboard = [
        ['','','',''],
        ['','','',''],
        ['','','',''],
        ['','','','']
        ]
        print_gameboard(gameboard)
        continue
    elif turn_counter == 16:
        print('Draw game!!!')
        print_gameboard(gameboard)
        gameboard = [
        ['','','',''],
        ['','','',''],
        ['','','',''],
        ['','','','']
        ]
        print_gameboard(gameboard)
        continue
    if turn == 'Y':
        turn = 'X'
    else:
        turn = 'Y'   
    print_gameboard(gameboard)