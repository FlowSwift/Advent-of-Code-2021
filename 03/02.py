"""
https://adventofcode.com/2021/day/3
"""
with open("03/input.txt") as file_hnd:
    bit_amount = 12  # every input/line is 12 bits
    oxygen_generator_rating = file_hnd.readlines()
    for i in range(bit_amount):
        counter_0 = 0
        counter_1 = 0
        if len(oxygen_generator_rating) <= 1:
            break
        for entry in oxygen_generator_rating:
            if entry[i] == "0":
                counter_0 += 1
            else:
                counter_1 += 1
        tmp_oxygen_rating = []
        if counter_0 > counter_1:
            for c, entry in enumerate(oxygen_generator_rating):
                if entry[i] == "0":
                    tmp_oxygen_rating.append(entry)
                else:
                    continue
        elif counter_1 > counter_0 or counter_1 == counter_0:
            for c, entry in enumerate(oxygen_generator_rating):
                if entry[i] == "1":
                    tmp_oxygen_rating.append(entry)
                else:
                    continue
        oxygen_generator_rating = tmp_oxygen_rating.copy()

with open("03/input.txt") as file_hnd:
    bit_amount = 12  # every input/line is 12 bits
    co2_rating = file_hnd.readlines()
    for i in range(bit_amount):
        counter_0 = 0
        counter_1 = 0
        if len(co2_rating) <= 1:
            break
        for entry in co2_rating:
            if entry[i] == "0":
                counter_0 += 1
            else:
                counter_1 += 1
        tmp_co2_rating = []
        if counter_1 > counter_0 or counter_1 == counter_0:
            for c, entry in enumerate(co2_rating):
                if entry[i] == "0":
                    tmp_co2_rating.append(entry)
                else:
                    continue
        elif counter_0 > counter_1:
            for c, entry in enumerate(co2_rating):
                if entry[i] == "1":
                    tmp_co2_rating.append(entry)
                else:
                    continue
        co2_rating = tmp_co2_rating.copy()
print(int(co2_rating[0].strip(), 2) * int(oxygen_generator_rating[0].strip(), 2))
