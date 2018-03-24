import sys
global count
count = 0
global blocks
blocks = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
global x_move
global o_move


def turn():
    global count
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(blocks[0], blocks[1], blocks[2]))
    print('_____|_____|_____')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(blocks[3], blocks[4], blocks[5]))
    print('_____|_____|_____')
    print('     |     |     ')
    print('  {}  |  {}  |  {}  '.format(blocks[6], blocks[7], blocks[8]))
    print('     |     |     ')
    if checkWin() == 'x':
        print('X wins')
        sys.exit()
    elif checkWin() == 'o':
        print('O wins')
        sys.exit()
    if count % 2:
        print('X\'s turn')
        x_move = int(input('Enter square number: '))
        # Todo: add input verification
        # while ((x_move < 0) or (x_move > 9)) or ((0 < x_move < 9) and (blocks[x_move] != ' ')):
        #    print('Invalid move, try again')
        #    x_move = int(input('Enter square number: '))
        blocks[int(x_move)] = 'X'
    else:
        print('O\'s turn')
        o_move = int(input('Enter square number: '))
        # while ((o_move < 0) or (o_move > 9)) or ((0 < o_move < 9) and (blocks[o_move] != ' ')):
        #    print('Invalid move, try again')
        #    x_move = int(input('Enter square number: '))
        blocks[int(o_move)] = 'O'
    count += 1
    turn()


def checkWin():
    # Horizontal Cases
    if blocks[0] == blocks[1] == blocks[2] != ' ':
        if blocks[0] == 'X':
            return 'x'
        else:
            return 'o'
    elif blocks[3] == blocks[4] == blocks[5] != ' ':
        if blocks[0] == 'X':
            return 'x'
        else:
            return 'o'
    elif blocks[6] == blocks[7] == blocks[8] != ' ':
        if blocks[0] == 'X':
            return 'x'
        else:
            return 'o'
    # Vertical Cases
    elif blocks[0] == blocks[3] == blocks[6] != ' ':
        if blocks[0] == 'X':
            return 'x'
        else:
            return 'o'
    elif blocks[1] == blocks[4] == blocks[7] != ' ':
        if blocks[0] == 'X':
            return 'x'
        else:
            return 'o'
    elif blocks[2] == blocks[5] == blocks[8] != ' ':
        if blocks[0] == 'X':
            return 'x'
        else:
            return 'o'
    # Diagonal Cases
    elif blocks[0] == blocks[4] == blocks[8] != ' ':
        if blocks[0] == 'X':
            return 'x'
        else:
            return 'o'
    elif blocks[2] == blocks[4] == blocks[6] != ' ':
        if blocks[0] == 'X':
            return 'x'
        else:
            return 'o'

turn()
