import sys
import time


file = open("inputs\\test8-3.txt").read().splitlines()

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
    side: str,
    nodes: dict,
    actual_nodes: list,
    searched_node: str,
    index: int,
    steps_count: list,
):
    if all(node[2] == searched_node for node in actual_nodes):
        steps_count.append(0)
        return
    else:
        index = (index + 1) % len(instructions)

        next_nodes = [nodes[actual_node][side] for actual_node in actual_nodes]

        steps_count.append(1)

        return steps(
            instructions[index], nodes, next_nodes, searched_node, index, steps_count
        )


if __name__ == "__main__":
    nodes = to_dict(nodes_list)

    initial_nodes = [key for key in nodes.keys() if key[2] == "A"]

    # initial_nodes = ["MLA"]  # 'MLA', 'BQA', 'MJA', 'AAA', 'TGA', 'BJA'

    searched = "Z"
    steps_count = []

    sys.setrecursionlimit(100000)
    start_time = time.time()
    steps(instructions[0], nodes, initial_nodes, searched, 0, steps_count)
    print(sum(steps_count))
    print("--- %s seconds ---" % (time.time() - start_time))
