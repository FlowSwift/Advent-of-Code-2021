scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
closers = {")": "(", "]": "[", "}": "{", ">": "<"}
score = 0
with open("10/input.txt") as file_hnd:
    for line in file_hnd:
        openers = []
        for char in line:
            if char not in scores:
                openers.append(char)
            else:
                if closers[char] != openers[-1]:
                    ("ILLEGAL CHAR: " + char + ":" + str(scores[char]))
                    score += scores[char]
                    break
                else:
                    openers.pop()

print(score)