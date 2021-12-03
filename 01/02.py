with open('01/input.txt') as file_hnd:
    numbers = [int(line.strip()) for line in file_hnd]
increments = 0
for i in range(len(numbers) - 2):
    if sum(numbers[i:i+3]) < sum(numbers[i+1:i+4]):
        increments += 1
print(increments)
