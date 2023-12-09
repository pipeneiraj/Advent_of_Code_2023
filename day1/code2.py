# crear la lista donde guardar las filas del archivo
lines = []

# abrir el archivo
with open("day1\input.txt") as file:
    for row in file:
        lines.append(row.rstrip())  # guardar las filas en la lista

index = 0
for line in lines:
    new = line
    if "one" in line:
        line = line.replace("one", "o1e")
    if "two" in line:
        line = line.replace("two", "t2o")
    if "three" in line:
        line = line.replace("three", "t3e")
    if "four" in line:
        line = line.replace("four", "f4r")
    if "five" in line:
        line = line.replace("five", "f5e")
    if "six" in line:
        line = line.replace("six", "s6x")
    if "seven" in line:
        line = line.replace("seven", "s7n")
    if "eight" in line:
        line = line.replace("eight", "e8t")
    if "nine" in line:
        line = line.replace("nine", "n9e")
    lines[index] = line
    index += 1

print(lines)

# crear la lista donde guardar los "codigos"
nums = []
for line in lines:
    digits = []  # crear la lista para guardar los digitos de la fila
    for word in line:
        if word.isdigit():
            digits.append(int(word))
    calibration = digits[0] * 10 + digits[len(digits) - 1]
    nums.append(calibration)

print(nums)

print(sum(nums))
