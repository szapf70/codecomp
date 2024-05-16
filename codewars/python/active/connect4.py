# https://www.codewars.com/kata/56882731514ec3ec3d000009
# Connect Four


def check(field,c):
    # Check rows
    for r in range(6):
        for c in range(3):
            if set(field[r][c:c+4]) == {c}:
                return c
    
    # create l and right shifted field 
    print("-----")
    for l in list(zip(*field[::-1])):
        print(l)
    

def who_is_winner(moves):
    field = [
                ['_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_'],
                ['_','_','_','_','_','_','_']
            ] 
    c = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6}
    h = [5,5,5,5,5,5,5]

    w = {"R" : "Red", "Y" : "Yellow"}

    for m in moves:
        column, color = m.split('_')
        if h[c[column]] >= 0:
            field[h[c[column]]][c[column]] = color[0]
            h[c[column]] -= 1
        ans = check(field,color[0])
        if ans != None:
            return w[ans]
    
    
    
    return field

moves = [
            "A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red",
            "G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
        ]

for l in who_is_winner(moves):
    print(l)