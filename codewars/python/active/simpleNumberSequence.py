# https://www.codewars.com/kata/5a28cf591f7f7019a80000de/train/python
# Simple number sequence

import sys
def check_slope(nstr, l):
    a = int(nstr[:l])
    b = int(nstr[l:l*2])
    if b == a+1:
        return a,b
    else:
        return None 

def missing(s):
    for l in range(1,len(s)//2):
        cs = check_slope(s,l)
        if cs




    else:
        return -1
            
    while l < len(s)//2 and not check_slope(s,l) 




print(check_slope('899091939495',2))


sys.exit()


print(missing("123567"),4)
print(missing("899091939495"),92)
print(missing("9899101102"),100)
print(missing("599600601602"),-1)
print(missing("8990919395"),-1)
print(missing("998999100010011003"),1002)
print(missing("99991000110002"),10000)
print(missing("979899100101102"),-1)
print(missing("900001900002900004900005900006"),900003)