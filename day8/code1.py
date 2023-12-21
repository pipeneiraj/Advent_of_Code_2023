import sys

with open("inputs\\input8.txt") as f:
    file = f.read().splitlines()


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


def steps(side: str, actual_node: str, search_node: str, index: int) -> int:
    if actual_node == search_node:
        return 0
    else:
        index = (index + 1) % len(instructions)

        next_node = nodes[actual_node][side]

        return 1 + steps(
            instructions[index],
            next_node,
            search_node,
            index,
        )


if __name__ == "__main__":
    nodes = to_dict(nodes_list)

    initial = "AAA"
    searched = "ZZZ"

    sys.setrecursionlimit(20000)
    print(steps(instructions[0], initial, searched, 0))
