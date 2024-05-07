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
step = instr_ptr = 0
act = "AAA"
while act != "ZZZ":
    act = elements[act][instr[instr_ptr]]
    instr_ptr += 1
    instr_ptr %= len(instr)
    step += 1

   
print(step, "Steps")
