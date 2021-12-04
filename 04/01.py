"""
https://adventofcode.com/2021/day/4
"""
def calc_answer(board,last_num):
    """
    Find the answer by doing a sum of all the unmarked numbers in the winning board and multiply by the last num
    """
    sum = 0
    for row in board:
        for num in row:
            if num != "x":
                sum += int(num)
    print(sum*int(last_num))

def winner_info(c, num, board):
    print(c)
    print(num)
    print(board)
    calc_answer(board, num)
    exit()

with open("04/input.txt") as file_hnd:
    lines = file_hnd.readlines()
    boards = []
    board = []
    for line in lines[2:]:  # read the boards from input into boards, new board start on a new line
        if line.strip() == "":
            boards.append(board)
            board = []
        else:
            board.append(line.split())
    for num in lines[0].split(","):
        for c, board in enumerate(boards):  # iterate all boards, mark numbers and check if winner after
            for row in board:
                if num in row:
                    row[row.index(num)] = "x"  # mark number if found
            for i in range(5):  # check win condition for horizontal lines
                win = True
                for j in range(5):
                    if board[i][j] != "x":
                        win = False
                if win:
                    winner_info(c, num, board)
            for i in range(5):  # check win condition for vertical lines
                win = True
                for j in range(5):
                    if board[j][i] != "x":
                        win = False
                if win:
                    winner_info(c, num, board)