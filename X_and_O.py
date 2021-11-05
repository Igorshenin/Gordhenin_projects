a = ['-', '-', '-']
b = ['-', '-', '-']
c = ['-', '-', '-']
game_vars = ['Победил крестик',
            'Победил нолик',
            'Победила дружба',
            'Сюда ходить нельзя!!!',
            'Game over',
            '   0 1 2',
            '----------',
            'Значение хода неверное!!!',
            'Введи колонку и строку без пробела (q - сдаться) = '
            ]
who = ['O', 'X', 'Ход нолика', 'Ход крестика']
comb = ['00', '01', '02',
        '10', '11', '12',
        '20', '21', '22',
        'q'
        ]
count_move = 0
win = 0
symb, move_symb = who[1], who[3]


def print_win(winner):
    print(winner)
    return


def check_to_win(aa, bb, cc, win_):
    a1, b1, c1 = list(zip(aa, bb, cc))
    if aa.count(who[1]) == 3 or bb.count(who[1]) == 3 or cc.count(who[1]) == 3:
        print_win(game_vars[0])
        win_ += 1
    elif aa.count(who[0]) == 3 or bb.count(who[0]) == 3 or cc.count(who[0]) == 3:
        print_win(game_vars[1])
        win_ += 1
    elif a1.count(who[1]) == 3 or b1.count(who[1]) == 3 or c1.count(who[1]) == 3:
        print_win(game_vars[0])
        win_ += 1
    elif a1.count(who[0]) == 3 or b1.count(who[0]) == 3 or c1.count(who[0]) == 3:
        print_win(game_vars[1])
        win_ += 1
    elif aa[0] == who[1] and bb[1] == who[1] and cc[2] == who[1]:
        print_win(game_vars[0])
        win_ += 1
    elif aa[2] == who[1] and bb[1] == who[1] and cc[0] == who[1]:
        print_win(game_vars[0])
        win_ += 1
    elif aa[0] == who[0] and bb[1] == who[0] and cc[2] == who[0]:
        print_win(game_vars[1])
        win_ += 1
    elif aa[2] == who[0] and bb[1] == who[0] and cc[0] == who[0]:
        print_win(game_vars[1])
        win_ += 1
    elif aa.count('-') == 0 and bb.count('-') == 0 and cc.count('-') == 0:
        print_win(game_vars[2])
        win_ += 1
    return win_


def check_empty(aa, col, symb, count_func):
    if aa[col] != "-":
        print(game_vars[3])
    else:
        aa[col] = symb
        count_func += 1
    return count_func


def who_move(who_count, s, s1):
    if who_count % 2 == 0:
        s, s1 = who[1], who[3]
    else:
        s, s1 = who[0], who[2]
    return s, s1


def game_board(aa, bb, cc):
    i = 0
    print(game_vars[5])
    print(game_vars[6])
    for x, y, z in aa, bb, cc:
        print(f"{i}| {x} {y} {z} |")
        i += 1
    print(game_vars[6])

while True:
    win = check_to_win(a, b, c, win)
    game_board(a, b, c)

    if win == 1:
        print(game_vars[4])
        break
    symb, move_symb = who_move(count_move,symb, move_symb)

    while True:
        print(move_symb)
        move_gamer = input(game_vars[8])
        if move_gamer in comb:
            break
        else:
            print(game_vars[7])
    if move_gamer == comb[9]:
        print(f"Юзер, играющий за '{symb}' сдался!")
        break
    else:
        move_gamer_col, move_gamer_row =[x for x in move_gamer]
        move_gamer_col, move_gamer_row = int(move_gamer_col), int(move_gamer_row)
        if move_gamer_row == 0:
            count_move = check_empty(a, move_gamer_col, symb, count_move)
        if move_gamer_row == 1:
            count_move = check_empty(b, move_gamer_col, symb, count_move)
        if move_gamer_row == 2:
            count_move = check_empty(c, move_gamer_col, symb, count_move)
