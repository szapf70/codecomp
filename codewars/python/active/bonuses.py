# https://www.codewars.com/kata/5d68d05e7a60ba002b0053f6/train/python
# Bonuses

def bonus(arr, s):
    boni = []
    all_abdays_inv = sum(1.0 / d for d in arr)
    for d in arr:
        id = 1.0 / d
        b = (id / all_abdays_inv) * s
        boni.append(round(b,0))
    return boni

#print(bonus([18,15,12], 851))
print(bonus([22,3,15], 18228))


    
    