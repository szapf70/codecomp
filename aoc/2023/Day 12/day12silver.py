from collections import defaultdict
import json
import sys



def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()

def recu(pattern,cnt,arrange):
    if cnt:
        i = pattern.find('?')
        return recu(pattern[0:i]+'#'+pattern[i+1:],cnt-1,arrange) + recu(pattern[0:i]+'.'+pattern[i+1:],cnt-1,arrange)
    else:
        larr = [len(n) for n in pattern.split('.')]
        larr = list(filter((0).__ne__, larr)) 
        #print(f"{larr} == {arrange} {larr==arrange} ")
        return arrange == larr
                
records_raw = load("input.txt")
records = []

for record in records_raw:
    rp = record.split()
    rp[1] = [int(c) for c in rp[1].split(',')]
    records.append(rp)
    
sum = 0    
for record in records:
    sum += recu(record[0],record[0].count('?'),record[1])

print(sum)