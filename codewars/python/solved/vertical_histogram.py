# https://www.codewars.com/kata/59cf0ba5d751dffef300001f/train/python
# Simple Fun #358: Vertical Histogram Of Letters

def vertical_histogram_of(s):
    ca = [[chr(l),s.count(chr(l))] for l in range(65,91) if s.count(chr(l)) > 0]
    rf = [[f[0] for f in ca]]
    s = 1
    used = True
    while used:
        lrf = []
        used = False
        for f in ca:
            if f[1] >= s:
                lrf.append('*')
                used = True
            else:
                lrf.append(' ')    

        if used:
            rf.insert(0,lrf)
            s += 1
        else:
            break    

    return "\n".join([" ".join(row).rstrip() for row in rf])



print(vertical_histogram_of('ABCDFFFGT'))