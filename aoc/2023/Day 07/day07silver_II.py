from collections import defaultdict
import json

def getconst(hand):
    constranks = {"5" : 7,"41" : 6,"32" : 5, "311" : 4, "221" : 3, "2111" : 2, "11111"  :1}
    lcnt = defaultdict(int)
    for card in hand:
        lcnt[card] += 1
    conste = "".join(sorted(list(map(str,lcnt.values())),reverse=True))
    constrank = constranks[conste]    
    return conste, constrank
    #return constranks[sorted(lcnt.values(),reverse=True)]

def compareconst(handa, handb):
    cv = {"2" : 2, "3" : 3,"4" :4, "5" :5,"6" :6,"7":7,"8":8,"9" : 9,"T" : 10, "J":11,"Q"  :12 ,"K" :13, "A":14}
    consta = getconst(handa)
    constb = getconst(handb)
    if consta < constb: return True
    if consta > constb: return False
    
    
    
    
    
    sa = 0
    sb = 0
    for i in range(0,5):
        sa += int(cv[handa[i]])*(10**((i*2)))
        sb += int(cv[handb[i]])*(10**((i*2)))
    print(handa,sa,handb,sb)

    if sa < sb: return True
    return False
        #sa += int(cv[handa[0]])*(10**(1+(i*2)))    
        #sb += int(cv[handb[0]])*(10**(1+(i*2)))    
    print(sa,sb)
"""
    consta = getconst(handa)
    constb = getconst(handb)
    if consta < constb: return True
    if consta > constb: return False
    for i in range(0,5):
        if cv[handa[i]] == cv[handb[i]]: continue
        if cv[handa[i]] < cv[handb[i]]: return True
        if cv[handa[i]] > cv[handb[i]]: return False
"""

def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()

lines = load("example.txt")
hands = []
for line in lines:
    lhand = {}
    lparts = line.split()
    lhand['cards'] = lparts[0]
    lhand['bid'] = int(lparts[1])
    hands.append(lhand)

for hand in hands:
    hand['const'], hand['constrank'] = getconst(hand['cards'])


#print(json.dumps(hands, indent=4))

for au_idx in range(1,len(hands)):
    for in_idx in range(au_idx+1,len(hands)):
        print(au_idx, in_idx)
        if compareconst(hands[in_idx]['cards'], hands[au_idx-1]['cards']):
            help = hands[au_idx]
            hands[au_idx] = hands[in_idx]
            hands[in_idx] = help

#print(json.dumps(hands, indent=4))

total_winnings  = 0
for i in range(0,len(hands)):
    hands[i]['winnings'] = hands[i]['bid'] * (i+1)
    total_winnings += hands[i]['winnings']
    print(f"{hands[i]['cards']}, {hands[i]['const']} Rank : {i+1}, {hands[i]['bid']},{hands[i]['winnings']},{total_winnings}")

 

print(total_winnings)    