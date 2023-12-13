# abrir el archivo
with open("inputs\\input4.txt") as file:
    content = file.read()
    lines = content.splitlines()  # guardar las filas en la lista


def to_dict(line):
    card, numbers = line.split(":")
    winners, card_numbers = numbers.split("|")
    return {
        "card": card,
        "winners": [int(i) for i in winners.split()],
        "card_numbers": [int(i) for i in card_numbers.split()],
    }


def search_numbers(dict):
    count = -1
    for win_number in dict["winners"]:
        count += dict["card_numbers"].count(win_number)
    if count < 0:
        return 0
    else:
        return 2**count


def test(line):
    return print(search_numbers(to_dict(line)))


if __name__ == "__main__":
    total_points = []

    for line, card in enumerate(lines):
        line_dict = to_dict(card)
        total_points.append(search_numbers(line_dict))

    print(sum(total_points))

    # test(lines[5])
