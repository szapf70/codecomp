# https://www.codewars.com/kata/59f4a0acbee84576800000af/train/python
# Positions Average

def pos_average(s):
    strs = s.split(', ')
    n = len(strs)
    cnt = (n*(n-1))/2
    all = cnt*len(strs[0])
    cp = 0
    p = len(strs) * len(strs[0])
    while len(strs) >= 1:
        act = strs.pop(0)
        for t in strs:
            print(act,t, act==t, cp)
            lcp = 0
            for i in range(len(act)):
                if act[i] == t[i]:
                    cp += 1

    return round(cp / all, 10)



print(pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"))
#print(pos_average("6900690040, 4690606946, 9990494604"))