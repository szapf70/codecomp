# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
# Battleship field validator

def validate_battlefield(field):
    # Anzahl belegter Felder muss 20 sein
    if sum([sum(f) for f in field]) != 20:
        return False
    
    # Schiffe suchen und zählen
    ships = [[],[],[],[],[]]
    seen = set()

    for y in range(10):
        for x in range(10):
            if (y,x) not in seen:
                seen.add((y,x))
                # Feld leer
                if not field[y][x]:
                    continue
                else:
                    # default is submarine
                    rl = 1
                    dl = 1
                    # check right for ship
                    while rl < 4 and x+rl <= 9 and field[y][x+rl]:
                        seen.add((y,x+rl))
                        rl += 1
                    # check down for ship
                    while dl < 4 and y+dl <= 9 and field[y+dl][x]:
                        seen.add((y+dl,x))
                        dl += 1

                    # count as sub marine
                    if rl == 1 and dl == 1:
                        ships[1].append(('r',rl,y,x))
                        continue

                    # check illegal positions
                    if rl > 1 and dl > 1:
                        return False
                    
                    # check ships greater submarin
                    if rl > 1:
                        ships[rl].append(('r',rl,y,x))
                    else:
                        ships[dl].append(('d',dl,y,x))        

    # valid shipcount
    if not len(ships[1]) == 4 or not len(ships[2]) == 3 or not len(ships[3]) == 2 or not len(ships[4]) == 1:
        return False

    # Ship count correct, now check invalid adjacents
    for sclass in ships:
        for ori,l,y,x in sclass:
            lpos = []
            if ori == 'r':
                lpos.append((y,x-1))
                lpos.append((y,x+l))
                for i in range(x-1,x+l+1):
                    lpos.append((y-1,i))
                    lpos.append((y+1,i))

            if ori == 'd':    
                lpos.append((y-1,x))
                lpos.append((y+l,x))
                for i in range(y-1,y+l+1):
                    lpos.append((i,x-1))
                    lpos.append((i,x+1))

            for y,x in lpos:
                if 0 <= y <= 9 and 0 <= x <= 9:
                    if field[y][x]:
                        return False

    return True

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField))