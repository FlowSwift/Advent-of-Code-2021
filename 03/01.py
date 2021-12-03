"""
https://adventofcode.com/2021/day/3
"""
with open("03/input.txt") as file_hnd:
    counter_list = [{0 : 0, 1 : 0} for i in range(12)]  # every input/line is 12 bits
    for line in file_hnd:
        for c, num in enumerate(line.strip()):  # find the most common number for each index in the line and store in a dict
            if num == "0":
                counter_list[c][0] += 1
            else:
                counter_list[c][1] += 1

gamma = ""
epsilon = ""
for dict in counter_list:  # check what was the most common number in each index and generate gamme and epsilon
    if dict[0] > dict[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
print(int(gamma, 2) * int(epsilon, 2))