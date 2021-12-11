
"""
https://adventofcode.com/2021/day/11
"""
#matrix = []
flashes = 0
def flash_check(fish_grid, row, column, flashed):
    global flashes
    if fish_grid[row][column] == 10:
        flashes += 1
        flashed.append((row,column))
        for i in range(row-1, row+2):
            for j in range(column-1, column+2):
                if i in range(len(fish_grid)) and j in range(len(fish_grid[i])) and (i,j) not in flashed:
                    if i == row and j == column:
                        continue
                    fish_grid[i][j] += 1
                    if flash_check(fish_grid, i, j, flashed):
                        fish_grid[i][j] = 0
        return True


with open("11/input.txt") as file_hnd:
    fish_grid = [[int(fish) for fish in line.strip()] for line in file_hnd]
    fish_amount = 0
    for line in fish_grid:
        fish_amount += len(line)
    cycles = 1000
    for cycle in range(cycles):
        flashed = []
        for row, line in enumerate(fish_grid):
            for column, fish in enumerate(line):
                fish_grid[row][column] += 1
                if flash_check(fish_grid, row, column, flashed):
                    fish_grid[row][column] = 0
        for fish in flashed:
            fish_grid[fish[0]][fish[1]] = 0
        if len(flashed) == fish_amount:
            print(cycle)

print(flashes)
