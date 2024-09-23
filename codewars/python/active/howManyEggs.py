# https://www.codewars.com/kata/58c1446b61aefc34620000aa/train/python
# How many eggs?

def egged(year, span):
    if year == 0:
        return "No chickens yet!"
    ckn = []    
    eggs = 0
    for y in range(year-1):
        for _ in range(3):
            ckn.append([300,span])
        print(eggs,ckn)    
        for i,c in enumerate(ckn):
            if c[1] > 0:
                eggs += c[0]
                ckn[i][0] = int(ckn[i][0]*0.8)
                ckn[i][1] -= 1
    return eggs   

print(egged(1,15))
         