"""
https://adventofcode.com/2021/day/13
"""
grid = {}
instructions = []
with open("13/input.txt") as file_hnd:
    max_x, max_y = 0,0
    for line in file_hnd:
        line = line.strip()
        if line == "":
            break
        pos = tuple(map(int, line.split(",")))
        # get the size of array
        if max_x == 0 or pos[0] > max_x:
            max_x = pos[0]
        if max_y == 0 or pos[1] > max_y:
            max_y = pos[1]+1
        grid[pos] = "marked"
    for line in file_hnd:
        instructions.append(line.strip())

for instruction in instructions:
    instruction_index = instruction.index("=")
    axis = instruction[instruction_index-1]
    fold_pos = int(instruction[instruction_index+1:])
    if fold_pos == 6:
        t_grid = [["." if (column,row) not in grid else "#" for column in range(max_x+1)] for row in range(max_y+1)]
        for line in t_grid:
            print("".join(line))
    tmp_grid = grid.copy()
    for pos in grid:
        if axis == "x":
            if pos[0] > fold_pos:
                tmp_grid[(abs(pos[0]-max_x),pos[1])] = "marked"
                tmp_grid.pop(pos)
        elif axis == "y":
            if pos[1] > fold_pos:
                tmp_grid[(pos[0],abs(pos[1]-max_y))] = "marked"
                tmp_grid.pop(pos)
    if axis == "x":
        max_x = (max_x//2) - 1
    elif axis == "y":
        max_y = (max_y//2) - 1
    grid = tmp_grid.copy()

print("--------")
print("--------")
print("--------")
grid = [["." if (column,row) not in grid else "#" for column in range(max_x+1)] for row in range(max_y+1)]
for line in grid:
    print("".join(line))