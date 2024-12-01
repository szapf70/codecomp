left = []
right = []
with open('silver.txt') as f:
    for line in f:
        parts = line.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

left = sorted(left)
right = sorted(right)
diffs = 0

for i in range(len(left)):
    
    diff = right[i] - left[i]
    diffs += abs(diff)

print(diffs)    
