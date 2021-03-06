"""
https://adventofcode.com/2021/day/7
"""
test_input = [16,1,2,0,4,2,7,1,2,14]

with open("07/input.txt") as file_hnd:
    inputs = list(map(int, file_hnd.read().strip().split(",")))
    #inputs = test_input
    fuel = []  # list of all the fuel needed to get to every position.
    current_total_fuel = 0
    for i in range(len(inputs)):
        for input in inputs:
            steps = abs(input - i)
            current_total_fuel += steps + sum(range(steps))  #for each step, fuel gets more expensive by 1
        fuel.append(current_total_fuel)
        current_total_fuel = 0

print(min(fuel))
print(fuel.index(min(fuel)))
