# https://www.codewars.com/kata/561c20edc71c01139000017c/train/python
# Organize a Round-robin tournament


"""
r1 = [1,2,3,4]
r2 = [8,7,6,5]
games = []
for _ in range(1,8):
    print(r1)
    print(r2)
    for i in range(0,4):
        games.append(str(r1[i]) + " vs. " + str(r2[i]))
    r2.append(r1.pop(-1))
    r1.insert(1,r2.pop(0))
print(len(games))    
"""

def build_matches_table(teams: int) -> list[list[(int, int)]]:
    t1 = [i for i in range(int(teams//2))]
    t2 = [i for i in range(int(teams//2),teams)]
    res = []
    for _ in range(teams-1):
        lres = []
        for i in range(len(t1)):
            lres.append((t1[i], t2[i]))
        res.append(lres)
        t2.append(t1.pop(-1))
        t1.insert(1,t2.pop(0))  
    return res      

print(build_matches_table(10))