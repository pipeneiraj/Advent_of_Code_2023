import math
import sys
import time

with open("inputs\\input8.txt") as f:
    file = f.read().splitlines()


instructions = file[0]

nodes_list = [
    file[i].replace("(", "").replace(")", "").split("=") for i in range(2, len(file))
]


def to_dict(nodes_list: list) -> dict:
    rules = {}
    for rule in nodes_list:
        left, right = rule[1].split()
        rules[rule[0].replace(" ", "")] = {"L": left.replace(",", ""), "R": right}
    return rules


def steps(side: str, actual_node: str, searched_node: str, index: int) -> int:
    if actual_node[2] == searched_node:
        return 0
    else:
        index = (index + 1) % len(instructions)

        next_node = nodes[actual_node][side]

        return 1 + steps(instructions[index], next_node, searched_node, index)


if __name__ == "__main__":
    start_time = time.time()
    nodes = to_dict(nodes_list)

    initial_nodes = [key for key in nodes.keys() if key[2] == "A"]

    searched = "Z"
    steps_count = []

    sys.setrecursionlimit(100000)

    for initial_node in initial_nodes:
        steps_count.append(steps(instructions[0], initial_node, searched, 0))

    print(math.lcm(*steps_count))

    print("--- %s seconds ---" % (time.time() - start_time))
