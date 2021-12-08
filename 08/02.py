import difflib

def remove_indexes(indexes, patterns):
    for i in sorted(indexes, reverse=True):
        patterns.pop(i)


def attempt1():
    with open("08/test_input.txt") as file_hnd:
        segments = {}
        sum = 0
        for line in file_hnd:
            patterns, digits = line.split(" | ")
            patterns = list(map(lambda s: "".join(sorted(s)), patterns.split()))
            digits = map(lambda s: "".join(sorted(s)), digits.split())
            indexes = []
            for i, pattern in enumerate(patterns):
                if len(pattern) == 2:
                    segments[1] = pattern
                    indexes.append(i)
                elif len(pattern) == 3:
                    segments[7] = pattern
                    indexes.append(i)
                elif len(pattern) == 4:
                    segments[4] = pattern
                    indexes.append(i)
                elif len(pattern) == 7:
                    segments[8] = pattern
                    indexes.append(i)
            remove_indexes(indexes, patterns)
            indexes = []
            for i, pattern in enumerate(patterns):
                if set(segments[4]) < set(pattern) and len(pattern) == 6:
                    segments[9] = pattern
                    indexes.append(i)
                elif set(segments[7]) < set(pattern) and len(pattern) == 5:
                    segments[3] = pattern
                    indexes.append(i)
            remove_indexes(indexes, patterns)
            indexes = []
            for i, pattern in enumerate(patterns):
                if set(segments[7]) < set(pattern) and len(pattern) == 6:
                    segments[0] = pattern
                    break
            patterns.pop(i)
            for i, pattern in enumerate(patterns):
                if len(pattern) == 6:
                    segments[6] = pattern
                    break
            patterns.pop(i)
            difference = difflib.ndiff(segments[1], segments[4])
            checker = ""
            for diff in difference:
                if diff.startswith("+"):
                    checker += diff[2:]
            for i, pattern in enumerate(patterns):
                if set(checker) < set(pattern) and len(pattern) == 5:
                    segments[5] = pattern
                    break
            patterns.pop(i)
            segments[2] = patterns[0]
            number = ""
            for digit in digits:
                for k,v in segments.items():
                    if v == digit:
                        number += str(k)
            sum += int(number)
    print(sum)


def attempt2():
    with open("08/test_input.txt") as file_hnd:
        segments = {}
        sum = 0
        for line in file_hnd:
            patterns, digits = line.split(" | ")
            patterns = list(map(lambda s: set("".join(sorted(s))), patterns.split()))
            digits = map(lambda s: set("".join(sorted(s))), digits.split())
            indexes = []
            for i, pattern in enumerate(patterns):
                if len(pattern) == 2:
                    segments[1] = pattern
                    indexes.append(i)
                elif len(pattern) == 3:
                    segments[7] = pattern
                    indexes.append(i)
                elif len(pattern) == 4:
                    segments[4] = pattern
                    indexes.append(i)
                elif len(pattern) == 7:
                    segments[8] = pattern
                    indexes.append(i)
            remove_indexes(indexes, patterns)
            indexes = []
            for i, pattern in enumerate(patterns):
                if len(pattern) == 6:
                    if len(segments[4] & pattern) == 4:
                        segments[9] = pattern
                    elif len(segments[7] & pattern) == 2:
                        segments[6] = pattern
                    else:
                        segments[0] = pattern
                elif len(pattern) == 5:
                    if len(segments[4] & pattern) == 2:
                        segments[2] = pattern
                    elif len(segments[7] & pattern) == 3:
                        segments[3] = pattern
                    else:
                        segments[5] = pattern
            number = ""
            for digit in digits:
                for k,v in segments.items():
                    if v == digit:
                        number += str(k)
            sum += int(number)
    print(sum)

attempt1()
attempt2()