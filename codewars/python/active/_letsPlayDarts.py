# https://www.codewars.com/kata/5870db16056584eab0000006/train/python
# Let's Play Darts!

import math


def get_score(x,y):
    vs = [(0,9,20),
          (9,27,1),
          (27,45,18),
          (45,63,4),
          (63,81,13),
          (81,99,6),
          (99,117,10),
          (117,135,15),
          (135,153,2),
          (153,171,17),
          (171,189,3),
          (189,207,19),
          (207,225,7),
          (225,243,16),
          (243,261,8),
          (261,279,11),
          (279,297,14),
          (297,315,9),
          (315,333,12),
          (333,351,5),
          (351,360,20)]

    d = ((x**2+y**2)**0.5)*2
    a = math.degrees(math.atan2(x,y))
    if d > 340:
        return "X"
    if d < 12.7:#
        return "DB"
    if d < 31.8:
        return "SB"
    
    res = ""
    if d >= 324 and d < 340:
        res += "D"
    if d >= 198 and d < 214:
        res += "T"     
    
    na = 0
    if a >= 0:
        na = a
    else:
        na = 360 - (-a)
   
    for s,e,v in vs:
        if s <= na < e:
            return res + str(v)
        

print(get_score(55.53,-87.95))