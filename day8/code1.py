import sys


file = open("inputs\\input8.txt").read().splitlines()

instructions = file[0]

nodes_list = [
    file[i].replace("(", "").replace(")", "").split("=") for i in range(2, len(file))
]

# nodes = {
#     key.replace(" ", ""): {
#         {"L": left, "R": right} for left, right in value.replace(",", "").split()
#     }
#     for key, value in [
#         file[i].replace("(", "").replace(")", "").split("=")
#         for i in range(2, len(file))
#     ]
# }


def to_dict(nodes_list: list) -> dict:
    rules = {}
    for rule in nodes_list:
        left, right = rule[1].split()
        rules[rule[0].replace(" ", "")] = {"L": left.replace(",", ""), "R": right}
    return rules


def steps(
    side: str, nodes: dict, actual_node: str, search_node: str, index: int
) -> int:
    if actual_node == search_node:
        return 0
    else:
        if index == len(instructions) - 1:
            index = 0
        else:
            index += 1
        return 1 + steps(
            instructions[index],
            nodes,
            nodes[actual_node][side],
            search_node,
            index,
        )


# def()

if __name__ == "__main__":
    nodes = to_dict(nodes_list)

    initial = "AAA"
    searched = "ZZZ"

    sys.setrecursionlimit(20000)
    print(steps(instructions[0], nodes, initial, searched, 0))
