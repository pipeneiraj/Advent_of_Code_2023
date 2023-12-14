file = open("inputs\\input6.txt").read().split()

time = [int(i) for i in file[1 : int(len(file) / 2)]]
distance = [int(i) for i in file[int(len(file) / 2) + 1 : len(file)]]

races = [[time[i], distance[i]] for i in range(0, len(time))]


def record(races: list[list[int]]) -> int:
    prod = 1
    for time, distance in races:
        sum = 0
        for i in range(1, time + 1):
            if (time - i) * i > distance:
                sum += 1
        prod *= sum
    return prod


if __name__ == "__main__":
    print(record(races))
