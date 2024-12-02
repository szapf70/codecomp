import itertools

reports = []

with open('day_02.txt') as f:
    for line in f:
        report = list(map(int,line.strip().split()))
        reports.append(report)
        
check = []
safe = 0

for r in reports:       
    lr = []
    for a,b in itertools.pairwise(r):
        lr.append(b-a)
    d = [e == -1 or e == -2 or e == -3 for e in lr]
    i = [e == 1 or e == 2 or e == 3 for e in lr]
    
    if all(d) or all(i):
        safe += 1
    
      
print(safe)        