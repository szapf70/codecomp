with open("input.txt", "r") as txt:
    game_lines = txt.read().splitlines()
    games = {}
    for game_line in game_lines:
        game_info = game_line.split(":")
        for game_set in game_info[1].split(";"):
            cl = ([tuple(color.split()) for color in game_set.split(",")])
            games.setdefault(int(game_info[0][5:]), []).append({key:int(value) for value, key in cl })

    id_sum = 0
    for game in games:
        possible = 1
        for set in games[game]:
            if not (set.setdefault('red', 0) <= 12 and set.setdefault('green', 0) <= 13 and set.setdefault('blue', 0) <= 14): possible = 0
        if possible: id_sum += game
    print(id_sum)    
