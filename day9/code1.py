input = open("inputs\\input9.txt").read().splitlines()

lines = [[int(x) for x in i.split()] for i in input]


def next_element(line: list) -> int:
    if all(num == 0 for num in line):
        return line[-1]
    else:
        diff = []
        for i in range(len(line) - 1):
            diff.append(line[i + 1] - line[i])
        return line[-1] + next_element(diff)


if __name__ == "__main__":
    next_elements = []
    for line in lines:
        next_elements.append(next_element(line))

    print(sum(next_elements))
