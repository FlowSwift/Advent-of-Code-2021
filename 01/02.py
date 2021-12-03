"""
https://adventofcode.com/2021/day/1
"""
with open('01/input.txt') as file_hnd:
    numbers = [int(line.strip()) for line in file_hnd]  # create a list of the input as integers
increments = 0
for i in range(len(numbers) - 3):  # loop over the input-3 to skip last group (3 inputs per group)
    if sum(numbers[i:i+3]) < sum(numbers[i+1:i+4]):  # check if the current 3 numbers are lower than the 3 numbers group from the next index
        increments += 1
print(increments)
