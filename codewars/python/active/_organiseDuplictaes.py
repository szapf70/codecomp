# https://www.codewars.com/kata/5884b6550785f7c58f000047/train/python
# Organise duplicate numbers in list

def group(arr):
    res = []
    for n in arr:
        print(res)
        stored = False
        
        for r in res:
            print(r)
            if r[0] == n:
                r.append(n)
                stored = True
                break 
        if not stored:
            res.append([n])        
    return res    

print(group([3,2,6,2,1,3]))    