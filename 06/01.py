"""
https://adventofcode.com/2021/day/6
"""
from collections import Counter

test_input = "3,4,3,1,2"
born_phase = 8  # when a fish is born
reset_phase = 6  # after phase 0
days = 80

def fish_calc1():
    with open("06/input.txt") as file_hnd:
        #fish = Counter(map(int, test_input.split(",")))
        fish = Counter(map(int, file_hnd.read().split(",")))
        for j in range(days):
            tmp_fish = fish.copy()
            for i in range(born_phase, -1, -1):
                if i == born_phase:  # always the amount of fishes that gave birth
                    fish[i] = tmp_fish[0]
                else:
                    if i == 0:  # ADD to the reset phase the amount of fishes from phase 0
                        fish[reset_phase] += tmp_fish[0]
                    fish[i] = tmp_fish[i+1]  # set phases 0-7
    return fish

def fish_calc2():
    with open("06/input.txt") as file_hnd:
        #fish = Counter(map(int, test_input.split(",")))
        fish = Counter(map(int, file_hnd.read().split(",")))
        for j in range(days):
            tmp_fish = fish.copy()
            fish[born_phase] = tmp_fish[0]  # always the amount of fishes that gave birth
            fish =  Counter({**fish, **{i: tmp_fish[i+1] if i != reset_phase else tmp_fish[reset_phase+1] + tmp_fish[0] for i in range(8)}})  # push all the fishes a phase and add to `fish` overwriting existing values`. Also add 0 to reset phase
    return fish

def fish_calc3():
    with open("06/input.txt") as file_hnd:
        #fish = Counter(map(int, test_input.split(",")))
        fish = Counter(map(int, file_hnd.read().split(",")))
        for j in range(days):
            tmp_fish = fish.copy()
            fish =  Counter({born_phase: tmp_fish[0]} | {i: tmp_fish[i+1] if i != reset_phase else tmp_fish[reset_phase+1] + tmp_fish[0] for i in range(8)})  # similar approach using union
    return fish
fish = fish_calc3()
print(sum([i for i in fish.values()]))