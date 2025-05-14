# https://www.codewars.com/kata/56882731514ec3ec3d000009
# Connect Four

def who_is_winner(moves):
    def draw(board,p):
        for y in range(5,-1,-1):
            line = ""
            for x in range(7):
                cell = board.get((x,y),'_')
                if p == '_':
                    line += cell
                else:
                    line += cell if cell == p else '_'    
            print(line)  
        print()      
    def all_check(p,board):
        for x in range(7):
            for y in range(6):
                if check(x,y,p,board):
                    return True
        return False
            
    def check(x,y,p,board):
        if x < 4: # Ho2Ri
            if board.get((x,y),'_') == board.get((x+1,y),'_') == board.get((x+2,y),'_') == board.get((x+3,y),'_') == p:
                print("Ho2Ri")
                return True
        if x > 2: # Ho2Le
            if board.get((x,y),'_') == board.get((x-1,y),'_') == board.get((x-2,y),'_') == board.get((x-3,y),'_') == p:
                print("Ho2Le")                
                return True
        if y < 3: #VeDo
            if board.get((x,y),'_') == board.get((x,y+1),'_') == board.get((x,y+2),'_') == board.get((x,y+3),'_') == p:
                print("VeDo")                
                return True
        if y > 2: #VeUp
            if board.get((x,y),'_') == board.get((x,y-1),'_') == board.get((x,y-2),'_') == board.get((x,y-3),'_') == p:
                print("VeUp")                
                return True

        if x < 4 and y < 3: # DiaRiDown
            if board.get((x,y),'_') == board.get((x+1,y+1),'_') == board.get((x+2,y+2),'_') == board.get((x+3,y+3),'_') == p:
                print("DiaRiDown")                
                return True

        if x > 2 and y < 3: # DiaLeUp
            if board.get((x,y),'_') == board.get((x-1,y-1),'_') == board.get((x-2,y-2),'_') == board.get((x-3,y-3),'_') == p:
                print("DiaLeUp")                
                return True

        if x < 4 and y > 2: # DiaRiUp
            if board.get((x,y),'_') == board.get((x+1,y-1),'_') == board.get((x+2,y-2),'_') == board.get((x+3,y-3),'_') == p:
                print("DiaRiUp")                
                return True

        if x < 4 and y > 2: # DiaLeDown
            if board.get((x,y),'_') == board.get((x-1,y+1),'_') == board.get((x-2,y+2),'_') == board.get((x-3,y+3),'_') == p:
                print("DiaLeDown")                
                return True

        return False    

    board = {}
    x = {'A' : 0,'B' : 1,'C' : 2,'D' : 3,'E' : 4,'F' : 5,'G' : 6}
    y = {'A' : 0,'B' : 0,'C' : 0,'D' : 0,'E' : 0,'F' : 0,'G' : 0}

    for m in moves:
        c,p = m[0], m[2]
        if y[c] < 6:
            board[(x[c], y[c])] = p
            draw(board,p)
            input("Taste drücken!")
            print(f"Check von {x[c]},{y[c]}")
            if all_check(p,board):
                return {'Y' : 'Yellow', 'R' : 'Red'}[p]
            y[c] += 1
    return "Draw"





moves = [
            "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red", 
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", 
"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red", 
"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red", 
"B_Yellow", "B_Red"
        ]

print(who_is_winner(moves))
