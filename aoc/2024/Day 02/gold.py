import itertools

def check(report):
    chg = []
    for a,b in itertools.pairwise(report):
        chg.append(b-a)
    d = [e == -1 or e == -2 or e == -3 for e in chg]
    i = [e == 1 or e == 2 or e ==3 for e in chg]  
    return all(d) or all(i)    
        

reports = []

with open('day_02.txt') as f:
    for line in f:
        report = list(map(int,line.strip().split()))
        reports.append(report)
        
safe = 0

for r in reports:  
    print(r)     
    if check(r):
        safe += 1
    else:
        lsafe = 0
        for i in range(len(r)):
            lr = r.copy()
            lr.pop(i)
            if check(lr):
                safe += 1
                break    
      
print(safe)        