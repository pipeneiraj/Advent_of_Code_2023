import time

with open("inputs\\input6.txt") as f:
    file = f.read().replace(" ", "").split()


time_ = int(file[0].split(":")[1])

distance = int(file[1].split(":")[1])

race = [time_, distance]


def record(race: list[int]) -> int:
    i = 0
    while (race[0] - i) * i < race[1]:
        i += 1
    sum = race[0] - i * 2 + 1
    return sum


if __name__ == "__main__":
    start_time = time.time()

    print(record(race))

    print("--- %s seconds ---" % (time.time() - start_time))
