with open("02/input.txt") as file_hnd:
    aim = 0
    distance = 0
    depth = 0
    for line in file_hnd:
        movements = line.split()
        if movements[0] == "forward":
            distance += int(movements[1])
            depth += aim * int(movements[1])
        elif movements[0] == "up":
            aim -= int(movements[1])
        elif movements[0] == "down":
            aim += int(movements[1])


print(depth * distance)