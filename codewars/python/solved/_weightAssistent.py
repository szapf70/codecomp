# https://www.codewars.com/kata/66ddde2d9d82c8517b575432/train/python
# Weight assistant

def assistance(weight):
    if weight == 20: return "Nothing to hang"
    if weight == 25: return "Only lock"
    
    if weight < 25: return "Error"

    weight = (weight - 25)/2
    out_l = []

    disks = [('red', 25), ('blue' , 20), ('yellow' , 15), ('green', 10),('black', 5),('orange', 2.5),('white', 1.25)]
    for d,w in disks:
        n = 0
        while weight >= w:
            n += 1
            weight -= w
        if n:
            out_l.append(f"{n} {d}{'s' if n>1 else ''}")
    out_l.append('lock')
    if weight == 0:
        return ", ".join(out_l)
    return "Error"


print(assistance(103))