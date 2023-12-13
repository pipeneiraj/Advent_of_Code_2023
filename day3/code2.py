# abrir el archivo
with open("inputs\\input3.txt") as file:
    content = file.read()
    lines = content.splitlines()  # guardar las filas en la lista


def find_numbers(k, line):
    numbers = []
    current_number = ""

    for i, char in enumerate(line):
        if not char.isdigit():
            if current_number:
                number_info = {
                    "number": int(current_number),
                    "line": k,
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
            "line": k,
            "f_index": len(line) - len(current_number),
            "l_index": len(line) - 1,
        }
        numbers.append(number_info)
    return numbers


def find_asterisk(k, line):
    asterisks = []
    for i, char in enumerate(line):
        if char == "*":
            asterisks_info = {"index": i, "line": k}
            asterisks.append(asterisks_info)
    return asterisks


def count_number(i, line, asterisk):
    i = 0
    for num in find_numbers(i, line):
        if (num["f_index"] - 1) <= asterisk["index"] and asterisk["index"] <= (
            num["l_index"] + 1
        ):
            touching.append(num["number"])  # touching number
            i += 1
    return i


def product_if_touching(touching):
    product = 1
    for number in touching:
        product *= number
    return products.append(product)


if __name__ == "__main__":
    products = []
    touching = []
    for i, line in enumerate(lines):
        asterisks_in_line = find_asterisk(i, line)
        for asterisk in asterisks_in_line:
            count = 0
            count += count_number(i - 1, lines[i - 1], asterisk)
            count += count_number(i, line, asterisk)
            count += count_number(i + 1, lines[i + 1], asterisk)
            if count == 2:
                product_if_touching(touching)
                touching.clear()
            else:
                touching.clear()

    print(sum(products))
