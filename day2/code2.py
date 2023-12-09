# abrir el archivo
with open("day2\input.txt") as file:
    content = file.read()
    lines = content.splitlines()  # guardar las filas en la lista

RED = 12  # 12 red cubes
GREEN = 13  # 13 green cubes
BLUE = 14  # 14 blue cubes

# crear el diccionario games ex: {Game 1: 7 blue, 5 red; 10 red, 7 blue; 5 blue, 4 green, 15 red; 4 green, 6 red, 7 blue; 5 green, 8 blue, 4 red; 5 red, 4 blue, 3 green}
games = {}  # key:value for key,value in lines.split(":",1)
for line in lines:
    key, value = line.split(":", 1)
    games[key] = value

# transformar en listas cada "sacada"
for game in games:
    games[game] = games[game].split(";")
    for i in range(len(games[game])):
        games[game][i] = games[game][i].split(",")

# comparar datos?
game_power = []
for game in games:
    red, green, blue = 0, 0, 0
    for i in range(len(games[game])):
        for j in range(len(games[game][i])):
            number, color = games[game][i][j].split()
            number = int(number)
            g, n_game = game.split()
            if color == "red":
                if number > red:
                    red = number
            elif color == "green":
                if number > green:
                    green = number
            elif color == "blue":
                if number > blue:
                    blue = number
    game_power.append(red * green * blue)

print(sum(game_power))
