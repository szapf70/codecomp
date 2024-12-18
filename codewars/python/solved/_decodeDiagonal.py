# https://www.codewars.com/kata/55af0d33f9b829d0a800008d/train/python
# Decode Diagonal

def get_diagonal_code(grid):
    lg = grid.replace(' ', '').split('\n')
    down = True
    r = 0
    p = 0
    res = ""
    while p < len(lg[r]):
        res += lg[r][p]
        p += 1
        if down:
            if r < len(lg)-1:        
                r += 1
            else:
                down = not down
                r -= 1            
        else:    
            if r > 0:
                r -= 1
            else:
                down = not down
                r += 1  
        print(r,p,len(grid[r]))
    return res

grid = "q z J H M z D v H B H A E D G x s C C t H K w y s G K I q L t K D E J w L\n" + \
        "K p v r v z C y K M o p D y o y r n\n" + \
        "M E w B C p F n M s M J E s u A r J G F L v t r F B H E E D y E x A z F L q s r"

print(get_diagonal_code(grid))            