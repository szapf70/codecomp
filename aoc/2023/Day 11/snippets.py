a = [3,0]
b = [7,8]

sa, sb = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])

koords = []

for s in range(sa+1, sb+1):
    koords.append((s,a[1]))
    
print(koords)

ea, eb = (a[1], b[1]) if a[1] < b[1] else (b[1], a[1])

for s in range(ea+1, eb+1):
    koords.append((b[0],s))

print(koords,len(koords))
    