with open("inputs\\input9.txt") as f:
    input = f.read().splitlines()


lines = [[int(x) for x in i.split()] for i in input]


def next_element(line: list) -> int:
    if all(num == 0 for num in line):
        return line[-1]
    else:
        diff = [line[i + 1] - line[i] for i in range(len(line) - 1)]

        return line[-1] + next_element(diff)


if __name__ == "__main__":
    next_elements = [next_element(line) for line in lines]

    print(sum(next_elements))
