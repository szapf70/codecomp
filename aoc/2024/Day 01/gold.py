left = []
right = []
with open('silver.txt') as f:
    for line in f:
        parts = line.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

rc = {}
for n in right:
    rc[n] = rc.get(n,0) + 1

simscore = 0

for n in left:
    simscore += n * rc.get(n,0)


print(simscore)    
