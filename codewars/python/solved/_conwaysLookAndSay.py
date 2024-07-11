# https://www.codewars.com/kata/530045e3c7c0f4d3420001af/train/python
# Conway's Look and Say - Generalized

def look_say(n):
    nstr = list(str(n))
    pre = []
    while len(nstr) > 0:
        first = nstr.pop(0)
        c = 1
        if len(nstr) > 0:
            while len(nstr) > 0 and nstr[0] == first:
                nstr.pop(0)
                c += 1
        pre.append((first,c))
    res = "" 
    for n,c in pre:
        res += str(c)+n
    return int(res)           

#print(look_say(21))
print(look_say(33333333333331),13311)


