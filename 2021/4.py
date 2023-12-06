
# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?


from os import WIFCONTINUED


cmds = []
boards = []
with open('4.data') as f:
    picks = f.readline().split(',')
    
    board = []
    for x in f.readlines():
        x = x.strip()
        if x:
            board.append(x.split())
        elif board:
            boards.append(board)
            board = []

if board:
    boards.append(board)
    board = []



def is_win(board):
    for i in range(5):
        unbroken = False
        for j in range(5):
            if board[i][j] != 'x':
                unbroken = True
                break
        if not unbroken:
            return True

    for j in range(5):
        unbroken = False
        for i in range(5):
            if board[i][j] != 'x':
                unbroken = True
                break
        if not unbroken:
            return True
    return False


def mark_pick(board, pick):
    for r_index, row in enumerate(board):    
        for c_index, col in enumerate(row):
            if pick == board[r_index][c_index]:
                board[r_index][c_index] = 'x'
                return


def sum_board(board):
    s = 0
    for row in board:
        for j in row:
            if j != 'x':
                s += int(j)
    return s


won_boards = set()

winning_board = None
for i in picks:
    last_called = int(i)
    for b_index, b in enumerate(boards):
        if b_index in won_boards:
            continue
        mark_pick(b, i)
        if is_win(b):
            won_boards.add(b_index)
            if len(won_boards) == len(boards):
                winning_board = b
    if winning_board is not None:
        break

a = last_called * sum_board(winning_board)
print(a)