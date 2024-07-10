# https://www.codewars.com/kata/55f4e56315a375c1ed000159/train/python
# Numbers that are a power of their sum of digits

nl = [81]

def sdig(num):
    instr = list(str(num))
    return sum(list(map(int,instr)))**len(instr) == num

def power_sumDigTerm(n):
    while len(nl) < n:
        ln = nl[-1] + 1
        while not sdig(ln):
            print(ln,nl)
            ln += 1
        nl.append(ln)
            
    return nl[n-1]       
        
print(sdig(4913))

print(17*17*17)
#print(power_sumDigTerm(4))
