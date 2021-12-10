"""
https://adventofcode.com/2021/day/9
"""
with open("09/input.txt") as file_hnd:
    heights = [[int(j.strip()) for j in i[:-1]] for i in file_hnd]
    print(heights)
    risk = 0
    left_b = 0
    right_b = len(heights[0])-1
    upper_b = 0
    lower_b = len(heights)-1
    for row, line in enumerate(heights):  # check if neighbor isnt out of bounds then check if bigger than currect height. 
        for column, height in enumerate(heights[row]):
            if row > upper_b:
                if not heights[row-1][column] > height:
                    continue
            if row < lower_b:
                if not heights[row+1][column] > height:
                    continue
            if column > left_b:
                if not heights[row][column-1] > height:
                    continue
            if column < right_b:
                if not heights[row][column+1] > height:
                    continue
            risk += height + 1
            print(height)
            print("---------------")
print(risk)