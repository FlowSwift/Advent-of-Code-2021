import os

first = True
increments = 0
last_num = None
with open('01/input.txt') as file_hnd:
    for line in file_hnd:
        current_num = int(line.strip())
        if not first and current_num > last_num:
            increments += 1
        last_num = current_num
        first = False
print(increments)
