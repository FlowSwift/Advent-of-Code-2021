"""
https://adventofcode.com/2021/day/8
"""
with open("08/test_input.txt") as file_hnd:
    count = []
    for line in file_hnd:
        patterns, digits = line.split(" | ")
        digits = digits.split()
        [count.append(num) for num in digits if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7]
print(len(count))