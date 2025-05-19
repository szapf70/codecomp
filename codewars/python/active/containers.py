# https://www.codewars.com/kata/5b80dea49895f71f3e00002d/train/python
# Containers

from collections import Counter

def containers(inp):
    linp = list(inp)
    stacks = []
    cc = Counter(linp)
    while linp:
        stacks = sorted(stacks)
        print(stacks)
        c = linp.pop(0)
        cc[c] -= 1

        if stacks == []: 
            stacks.append(c)
            continue
        
        for i in range(len(stacks)):
            if (stacks[i][0] == c) or (stacks[i][0] > c and cc[stacks[i][0]] == 0):
                stacks[i] = c + stacks[i]    
                c = None
                break

        if c:
            stacks.append(c) 

    return len(stacks)          



print(containers('RKEZMVGUTABLOOBGTPJYMTCOTYDVSBZJZNZEYLYYZIZYHPIPPY'), 10)
#print(containers('A'), 1)
##print(containers('CBACBACBACBACBA'), 3)
#print(containers('CCCCBBBBAAAA'), 1)
#print(containers('CODEWARS'), 5)