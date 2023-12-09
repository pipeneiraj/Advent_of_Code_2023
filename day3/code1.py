# abrir el archivo
with open("day3\input.txt") as file:
    content = file.read()
    lines = content.splitlines()  # guardar las filas en la lista


def find_numbers(line):
    numbers = []
    current_number = ""

    for i, char in enumerate(line):
        if not char.isdigit():
            if current_number:
                number_info = {
                    "number": int(current_number),
                    "f_index": i - len(current_number),
                    "l_index": i - 1,
                }
                numbers.append(number_info)
                current_number = ""
        elif char.isdigit():
            current_number += char

    if current_number:
        number_info = {
            "number": int(current_number),
            "f_index": len(line) - len(current_number),
            "l_index": len(line) - 1,
        }
        numbers.append(number_info)

    return numbers


def find_symbols(line):
    symbols = []
    current_symbol = ""

    for i, char in enumerate(line):
        if not char.isascii() or char == "." or char.isalnum():
            if current_symbol:
                number_info = {"symbol": current_symbol, "index": i - 1}
                symbols.append(number_info)
                current_symbol = ""
        elif char.isascii() and char != "." and not char.isalnum():
            current_symbol += char

    if current_symbol:
        number_info = {"symbol": current_symbol, "index": len(line) - 1}
        symbols.append(number_info)

    return symbols


def save_number(line, num):
    for sym in find_symbols(line):
        if num["f_index"] - 1 <= sym["index"] and sym["index"] <= num["l_index"] + 1:
            valids.append(num["number"])


if __name__ == "__main__":
    valids = []
    for i, line in enumerate(lines):
        numbers = find_numbers(line)
        for num in numbers:
            save_number(line, num)
            if i < len(lines) - 1:
                save_number(lines[i + 1], num)
            if i > 0:
                save_number(lines[i - 1], num)

    print(sum(valids))
