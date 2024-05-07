from collections import defaultdict
import json
import sys


def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()
    
lines = load("input.txt")
instr = lines.pop(0)
lines.pop(0)

elements = {l[0:3] : {"L":l[7:10], "R":l[12:15]} for l in lines} 

fset = [item for item in elements if item.endswith('A')]
step = instr_ptr = 0
#print(fset)
while not all([f.endswith('Z') for f in fset]):
   
    for i in range(0, len(fset)):
        fset[i] = elements[fset[i]][instr[instr_ptr]]
    #print(fset)
    instr_ptr += 1
    instr_ptr %= len(instr)
    step += 1

   
print(step, "Steps")
