import time


with open("inputs\\input5.txt") as file:
    content = file.read()
    lines = content.splitlines()  # guardar las filas en la lista


def to_seeds(lines: list[str]) -> set[int]:
    seeds = lines[0].split()
    seeds.pop(0)
    lines.pop(0)
    seeds = {int(seed) for seed in seeds}
    return seeds


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


def search_ids(ids: set[int], maps: list[list[int]]) -> set[int]:
    return_ids = set()

    for i in ids:
        count = 0
        for m in maps:
            if m[1] <= i and i < m[1] + m[2]:
                # if id in range(m[1], m[1] + m[2]):
                return_ids.add(m[0] + (i - m[1]))
                count += 1
        if count == 0:
            return_ids.add(i)
    return return_ids


if __name__ == "__main__":
    start_time = time.time()

    seeds_id = to_seeds(lines)

    seed_to_soil, lines = to_list(lines)
    soil_to_fertilizer, lines = to_list(lines)
    fertilizer_to_water, lines = to_list(lines)
    water_to_light, lines = to_list(lines)
    light_to_temperature, lines = to_list(lines)
    temperature_to_humidity, lines = to_list(lines)
    humidity_to_location, lines = to_list(lines)

    # Search ids
    soil_ids = search_ids(seeds_id, seed_to_soil)
    fertilizer_ids = search_ids(soil_ids, soil_to_fertilizer)
    water_ids = search_ids(fertilizer_ids, fertilizer_to_water)
    light_ids = search_ids(water_ids, water_to_light)
    temperature_ids = search_ids(light_ids, light_to_temperature)
    humidity_ids = search_ids(temperature_ids, temperature_to_humidity)
    location_ids = search_ids(humidity_ids, humidity_to_location)

    print(min(location_ids))

    print("total--- %s seconds ---" % (time.time() - start_time))
    # print(seeds_id)
    # print(soil_ids)
    # print(fertilizer_ids)
    # print(water_ids)
    # print(light_ids)
    # print(temperature_ids)
    # print(humidity_ids)
    # print(location_ids)
