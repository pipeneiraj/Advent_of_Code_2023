import time
from typing import Any, Generator


with open("day5\\input.txt") as file:
    content = file.read()
    lines = content.splitlines()  # guardar las filas en la lista


def get_seeds_data(lines: list[str]) -> list[list[int]]:
    line = lines[0].split()
    line.pop(0)
    lines.pop(0)
    line = [int(i) for i in line]
    seeds_data = []
    for i in range(0, len(line), 2):
        seeds_data.append([line[i], line[i + 1]])
    return seeds_data


def to_list(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    data = []
    if len(lines[0]) == 0:
        lines.pop(0)
    for i, line in enumerate(lines):
        if len(line) == 0:
            lines = lines[i:]  # copia la lista desde el index actual en adelante
            return data, lines
        elif "map" in line:
            pass
        elif len(line) > 0:
            numbers = [int(i) for i in line.split(" ")]
            data.append(numbers)
    return data, lines


def to_generator(parameters: list[int]) -> Generator[Any, Any, Any]:
    for i in range(parameters[0], parameters[0] + parameters[1]):
        yield i


def search_id(id: int, maps: list[list[int]]) -> int:
    for m in maps:
        if m[1] <= id and id < m[1] + m[2]:
            return m[0] + (id - m[1])
    return id


if __name__ == "__main__":
    start_time = time.time()

    seeds_data = get_seeds_data(lines)

    seed_to_soil, lines = to_list(lines)
    soil_to_fertilizer, lines = to_list(lines)
    fertilizer_to_water, lines = to_list(lines)
    water_to_light, lines = to_list(lines)
    light_to_temperature, lines = to_list(lines)
    temperature_to_humidity, lines = to_list(lines)
    humidity_to_location, lines = to_list(lines)

    minimum = 0

    for seeds in seeds_data:
        print(seeds)
        seeds_id = to_generator(seeds)

        for seed in seeds_id:
            # Search ids
            soil_id = search_id(seed, seed_to_soil)
            fertilizer_id = search_id(soil_id, soil_to_fertilizer)
            water_id = search_id(fertilizer_id, fertilizer_to_water)
            light_id = search_id(water_id, water_to_light)
            temperature_id = search_id(light_id, light_to_temperature)
            humidity_id = search_id(temperature_id, temperature_to_humidity)
            location_id = search_id(humidity_id, humidity_to_location)

            if minimum == 0:
                minimum = location_id
            else:
                if location_id < minimum:
                    minimum = location_id
        print("--- %s seconds ---" % (time.time() - start_time))

    print(minimum)

    print("total--- %s seconds ---" % (time.time() - start_time))
