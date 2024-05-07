# https://www.codewars.com/kata/5d076515e102162ac0dc514e/train/python
# Baby shark lyrics generator

def baby_shark_lyrics_old():
    o = []
    def din(n): return n + "," + " doo" * 6
    for d in ["Baby shark","Mommy shark","Daddy shark","Grandma shark","Grandpa shark", "Let's go hunt"]:
        for _ in range(3):
            o.append(din(d))     
        o.append(d + "!")    
    o.append("Run away,…")
    return "\n".join(o)

def baby_shark_lyrics():
    o = []
    for e in ["Baby shark","Mommy shark","Daddy shark","Grandma shark","Grandpa shark", "Let's go hunt"]:
        for _ in range(3): o.append(e+","+" doo"*6)     
        o.append(e+"!")    
    o.append("Run away,…")
    return "\n".join(o)



print(baby_shark_lyrics())


               