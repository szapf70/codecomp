# https://www.codewars.com/kata/5b80dea49895f71f3e00002d/train/python
# Containers

from collections import Counter

def containers(inp):
    cs = []
    cnt = Counter(inp)
    for c in inp:
        if len(cs) == 0:
            cs.append([])


print(containers('A'), 1)
print(containers('CBACBACBACBACBA'), 3)
print(containers('CCCCBBBBAAAA'), 1)
print(containers('CODEWARS'), 5)