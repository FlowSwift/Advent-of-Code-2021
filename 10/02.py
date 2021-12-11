scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores_2 = {"(": 1, "[": 2, "{": 3, "<": 4}
closers = {")": "(", "]": "[", "}": "{", ">": "<"}
#openers = {"(": ")", "[": "]", "{": "}", "<": ">"}
all_scores = []
with open("10/input.txt") as file_hnd:
    for line in file_hnd:
        score = 0
        score_02 = 0
        opened = []
        for char in line.strip():
            if char not in scores:
                opened.append(char)
            else:
                if closers[char] != opened[-1]:
                    ("ILLEGAL CHAR: " + char + ":" + str(scores[char]))
                    score += scores[char]
                    break
                else:
                    opened.pop()
        if score == 0:
            for opener in reversed(opened):
                p = scores_2[opener]
                score_02 = score_02 * 5 + scores_2[opener]
            all_scores.append(score_02)
all_scores.sort()
print(all_scores[len(all_scores)//2])