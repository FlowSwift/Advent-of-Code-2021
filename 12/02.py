"""
https://adventofcode.com/2021/day/12
"""
from collections import Counter
map = {}  # graph of all nodes
with open("12/test_input.txt") as file_hnd:
    for line in file_hnd:
        nodes = line.strip().split("-")
        if nodes[0] not in map:
            map[nodes[0]] = []
        map[nodes[0]].append(nodes[1])
        if nodes[1] not in map:
            map[nodes[1]] = []
        map[nodes[1]].append(nodes[0])

visited = Counter()
completed_path = 0
check = False
def check_neighbors(current_node, visited, map, check):
    global completed_path
    for exit in current_node:
        tmp_check = check
        if exit == "end":
            completed_path += 1
            continue
        if exit == "start":
            continue
        if (exit.islower() and visited[exit] >= 1):
            if tmp_check:
                continue
            tmp_check = True
            tmp_visited = visited.copy()
            check_neighbors(map[exit], tmp_visited, map, tmp_check)
            continue
        tmp_visited = visited.copy()
        tmp_visited[exit] += 1
        check_neighbors(map[exit], tmp_visited, map, check)

check_neighbors(map["start"], visited, map, check)
print(completed_path)