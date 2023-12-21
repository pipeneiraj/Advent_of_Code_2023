import time

with open("inputs\\input6.txt") as f:
    file = f.read().split()

time_ = [int(i) for i in file[1 : int(len(file) / 2)]]
distance = [int(i) for i in file[int(len(file) / 2) + 1 : len(file)]]

races = [[time_[i], distance[i]] for i in range(0, len(time_))]


def record(races: list[list[int]]) -> int:
    prod = 1
    for time_, distance in races:
        sum = 0
        while (time_ - sum) * sum < distance:
            sum += 1
        prod *= time_ - sum * 2 + 1
    return prod


if __name__ == "__main__":
    start_time = time.time()

    print(record(races))

    print("--- %s seconds ---" % (time.time() - start_time))
