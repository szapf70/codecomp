f = [0,1]
r = 0

while f[-1] < 4_000_000:
    f.append(f[-1]+f[-2])
    if f[-1]%2==0:
        r += f[-1]

print(r)        