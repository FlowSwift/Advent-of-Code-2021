from collections import defaultdict, Counter

test_input = "3,4,3,1,2"
start_value = 8
days = 80
with open("06/input.txt") as file_hnd:
    #fish = Counter(map(int, test_input.split(",")))
    fish = Counter(map(int, file_hnd.read().split(",")))
    for i in range(days):
        tmp_fish = fish.copy()
        for i in range(start_value, -1, -1):
            if i == start_value:
                fish[i] = tmp_fish[0]
            else:
                if i == 0:
                    fish[6] += tmp_fish[0]
                fish[i] = tmp_fish[i+1]

print(sum([i for i in fish.values()]))