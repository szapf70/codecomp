# https://www.codewars.com/kata/591aa1752afcb02fa300002a/train/python
# Thue-Morse Sequence

mc = ['0']

def gn():
    lmc = ''
    for c in mc[-1]:
        lmc += {'0' : '01', '1' : '10'}[c]
    mc.append(lmc)    

def thue_morse(n):
    while len(mc[-1]) < n: gn()
    return mc[-1][:n]

print(thue_morse(5))    