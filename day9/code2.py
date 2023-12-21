with open("inputs\\input9.txt") as f:
    input = f.read().splitlines()


lines = [[int(x) for x in i.split()] for i in input]


def previous_element(line: list) -> int:
    if all(num == 0 for num in line):
        return line[-1]
    else:
        diff = [line[i] - line[i + 1] for i in range(len(line) - 1)]

        return line[-1] - previous_element(diff)


if __name__ == "__main__":
    previous_elements = []

    for line in lines:
        line.reverse()
        previous_elements.append(previous_element(line))

    print(sum(previous_elements))
