boardnum = ['1', '2', '3', '4', '5', '6', '7','8', '9']


def Board():
    print('\n -----')
    print('|' + boardnum[0] + '|' + boardnum[1] + '|' + boardnum[2] + '|')
    print(' -----')
    print('|' + boardnum[3] + '|' + boardnum[4] + '|' + boardnum[5] + '|')
    print(' -----')
    print('|' + boardnum[6] + '|' + boardnum[7] + '|' + boardnum[8] + '|')
    print(' -----\n')


player1 = True
win = False

while not win:
    Board()

    if player1:
        print("Player 1: ")
    else:
        print("Player 2: ")

    try:
        pos = int(input("Position: "))
        if pos > 9:
            raise ValueError
            continue
    except ValueError:
        print("Enter valid input field")
        continue

    if boardnum[pos - 1] == 'X' or boardnum[pos - 1] == '0':
        print("Illegal move")
        continue

    if player1:
        boardnum[pos - 1] = 'X'
    else:
        boardnum[pos - 1] = '0'

    player1 = not player1

    for x in range(0, 3):
        y = x * 3
        if (boardnum[y] == boardnum[(y + 1)] and boardnum[y] == boardnum[(y + 2)]):
            win = True
            Board()
        if (boardnum[x] == boardnum[(x + 3)] and boardnum[x] == boardnum[(x + 6)]):
            win = True
            Board()

    if ((boardnum[0] == boardnum[4] and boardnum[0] == boardnum[8]) or
            (boardnum[2] == boardnum[4] and boardnum[4] == boardnum[6])):
        win = True
        Board()

print("Player " + str(int(player1 + 1)) + " wins!\n")
