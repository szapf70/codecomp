with open("input.txt", "r") as txt:
    game_lines = txt.read().splitlines()
    games = {}
    for game_line in game_lines:
        game_info = game_line.split(":")
        for game_set in game_info[1].split(";"):
            cl = ([tuple(color.split()) for color in game_set.split(",")])
            games.setdefault(int(game_info[0][5:]), []).append({key:int(value) for value, key in cl })

    sum_of_powers = 0
    for game in games:
        mins = {'red' : 0, 'green' : 0, 'blue' : 0}
        for set in games[game]:
            for min in mins:
                if set.setdefault(min, 0) >  mins[min]: mins[min] = set.setdefault(min, 0)
        sum_of_powers += mins['red'] * mins['green'] * mins['blue']    
    print(sum_of_powers)    
