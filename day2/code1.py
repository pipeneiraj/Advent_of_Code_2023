# abrir el archivo
with open("inputs\\input2.txt") as file:
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
valid_games = {i for i in range(1, 101)}
for game in games:
    for i in range(len(games[game])):
        for j in range(len(games[game][i])):
            number, color = games[game][i][j].split()
            number = int(number)
            g, n_game = game.split()
            if color == "red":
                if number > RED:
                    valid_games.discard(int(n_game))
                    break
            elif color == "green":
                if number > GREEN:
                    valid_games.discard(int(n_game))
                    break
            elif color == "blue":
                if number > BLUE:
                    valid_games.discard(int(n_game))
                    break

print(sum(valid_games))
