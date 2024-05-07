# 3 kyu https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
# Battleship field validator

def validate_battlefield(field):
    for i in range(len(field)):
        field[i].insert(0,0)
        field[i].insert(0,0)
        field[i].append(0)
        field[i].append(0)
    field.insert(0, [0] * len(field[0]))
    field.insert(0, [0] * len(field[0]))
    field.append([0] * len(field[0]))
    field.append([0] * len(field[0]))
    # count borders
    p = 0
    for x in range(1,len(field[0])-1):
        for y in range(1, len(field)-1):
            if field[y][x] == 0:
                lp = 0
                v = 0
                h = 0
                if field[y-1][x] == 1: 
                    p += 1
                    v += 1
                if field[y+1][x] == 1: 
                    p += 1
                    v += 1
                if field[y][x-1] == 1: 
                    p += 1
                    h += 1
                if field[y][x+1] == 1: 
                    p += 1
                    h += 1
                if lp > 2 : return False
                if lp == 2 : 
                    if v == 1 : return False

    # write your magic here
    return p == 60

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

"""
def land_perimeter(arr):

    p = 0

    for x in range(1,len(arr[0])-1):
        for y in range(1, len(arr)-1):
            if arr[y][x] == "O":
                if arr[y-1][x] == "X": p += 1
                if arr[y+1][x] == "X": p += 1
                if arr[y][x-1] == "X": p += 1
                if arr[y][x+1] == "X": p += 1

    return f"Total land perimeter: {p}"

"""