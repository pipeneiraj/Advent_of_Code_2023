#crear la lista donde guardar las filas del archivo
lines = [] 

# abrir el archivo
with open("day1\input.txt") as file:
    for row in file:
        lines.append(row.rstrip()) # guardar las filas en la lista

#crear la lista donde guardar los "codigos"
nums = []
for line in lines:
    digits = [] #crear la lista para guardar los digitos de la fila
    for word in line:
        if word.isdigit():
            digits.append(int(word))
    calibration = digits[0]*10 + digits[len(digits)-1]
    nums.append(calibration)

print(sum(nums))