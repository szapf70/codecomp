# Sums of Perfect Squares
# https://www.codewars.com/kata/5a3af5b1ee1aaeabfe000084/train/python


ps = []


def fillps():
    n = 1
    while True:
        ln = n**2
        if ln > 1_000_000_000:
            break
        ps.insert(0,ln)
        n += 1
    return    

def sum_of_squares(n):
    if ps == [] : fillps()  
    ps_store = []  
    ps_cnt = 0
    idx = 0
    while n > 0 and idx < len(ps):
        if n >= ps[idx]:
            n -= ps[idx]
            ps_store.append(ps[idx])
            ps_cnt += 1
            continue
        idx += 1 

    
    return ps_cnt


print(sum_of_squares(18))
#print(ps[0],ps[-1])
#print(len(ps))

"""Examples:

sum_of_squares(17) = 2
17 = 16 + 1 (16 and 1 are perfect squares).
sum_of_squares(15) = 4
15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
sum_of_squares(16) = 1
16 itself is a perfect square."""