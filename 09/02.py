
"""
https://adventofcode.com/2021/day/9
"""
#recursive approach
def check_edges(row, column, checked):
    checked.append(str(row) + "," + str(column))
    check = True
    global basin_size
    if row > upper_b:
        if not heights[row-1][column] > height:
            check = False
        if heights[row-1][column] < 9:
            if (str(row-1) + "," + str(column)) not in checked:
                basin_size += 1
                check_edges(row-1, column, checked)
    if row < lower_b:
        if not heights[row+1][column] > height:
            check = False
        if heights[row+1][column] < 9:
            if (str(row+1) + "," + str(column)) not in checked:
                basin_size += 1
                check_edges(row+1, column, checked)
    if column > left_b:
        if not heights[row][column-1] > height:
            check = False
        if heights[row][column-1] < 9:
            if (str(row) + "," + str(column-1)) not in checked:
                basin_size += 1
                check_edges(row, column-1, checked)
    if column < right_b:
        if not heights[row][column+1] > height:
            check = False
        if heights[row][column+1] < 9:
            if (str(row) + "," + str(column+1)) not in checked:
                basin_size += 1
                check_edges(row, column+1, checked)
    return check

with open("09/input.txt") as file_hnd:
    heights = [[int(j.strip()) for j in i[:-1]] for i in file_hnd]
    #boundries
    left_b = 0
    right_b = len(heights[0])-1
    upper_b = 0
    lower_b = len(heights)-1
    basins = []
    basin_size = 0
    for row, line in enumerate(heights):
        for column, height in enumerate(heights[row]):
            checked = []
            basin_size = 1
            if not check_edges(row, column,checked):
                continue
            basins.append(basin_size)
print(basins)
biggest = sorted(basins)[-3:]
print(biggest[0] * biggest[1] * biggest[2])