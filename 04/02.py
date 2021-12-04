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
    boards_amount = len(boards)
    winners = set()  # set of the current round(num iteration) winners
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
                    if len(boards) == 1:  # check if its the last board that won
                        winner_info(c, num, board)
                    winners.add(c)
            for i in range(5):  # check win condition for vertical lines
                win = True
                for j in range(5):
                    if board[j][i] != "x":
                        win = False
                if win:
                    if len(boards) == 1:  # check if its the last board that won
                        winner_info(c, num, board)
                    winners.add(c)
        #  once all boards marked in the num iteration remove all the boards that won if any
        winners_lst = list(winners)
        for winner in sorted(winners_lst, reverse=True):
            boards.pop(winner)
        winners = set()
