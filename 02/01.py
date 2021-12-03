"""
https://adventofcode.com/2021/day/2
"""
with open("02/input.txt") as file_hnd:
    forward = 0
    depth = 0
    for line in file_hnd:
        movements = line.split()
        #  check inputs and increment the respective variable
        if movements[0] == "forward":
            forward += int(movements[1])
        elif movements[0] == "up":
            depth -= int(movements[1])
        elif movements[0] == "down":
            depth += int(movements[1])


print(depth * forward)