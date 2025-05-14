# https://www.codewars.com/kata/6087bb6050a6230049a068f1/train/python
# Columnize

def columnize(items, cc):
    s = [0] * cc
    c = []

    while items:
        c.append(items[:cc])
        items = items[cc:]
    
    for l in c:
        for si in range(len(l)):
            if len(l[si]) > s[si]:
                s[si] = len(l[si])

    for ci in range(len(c)):
        for cci in range(len(c[ci])):
            c[ci][cci] = c[ci][cci].ljust(s[cci])

    return "\n".join([" | ".join(l) for l in c])

print(columnize(["1", "12", "123", "1234", "12345", "123456"], 4))

