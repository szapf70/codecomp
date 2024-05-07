from collections import defaultdict
import json
import sys


def jokerizer(cards):
    



def getconst(hand):
    lhand = hand
    constranks = {"5" : 7,"41" : 6,"32" : 5, "311" : 4, "221" : 3, "2111" : 2, "11111"  :1}
    cv = {"2" : 2, "3" : 3,"4" :4, "5" :5,"6" :6,"7":7,"8":8,"9" : 9,"T" : 10, "J":11,"Q"  :12 ,"K" :13, "A":14}

    lcnt = defaultdict(int)
    for card in hand:
        lcnt[card] += 1
    
    if 'J' in lcnt.keys():
        print("Jokerize",hand)
        j = lcnt['J']
        del lcnt['J']
        print(lcnt)
        bcard = ""
        bvalue = 0
    
        for card in lcnt:
            lvalue = lcnt[card]*cv[card]
             
            if lvalue > bvalue and j == lcnt[card]:
                bvalue = lvalue
                bcard = card
    
        lcnt[bcard] += j            
        lhand = lhand.replace('J', bcard)
        if len(lhand) != 5:
            print(f"|{hand}|{lhand}|, {j},{bcard}, {bvalue}, {lcnt}")
            sys.exit()
    
    #print(hand,lhand, lcnt)
    
    
    
    conste = "".join(sorted(list(map(str,lcnt.values())),reverse=True))
    constrank = constranks[conste]
    return conste,constrank,lhand
    #return constranks[sorted(lcnt.values(),reverse=True)]

def compareconst(handa, handb):
    cv = {"2" : 2, "3" : 3,"4" :4, "5" :5,"6" :6,"7":7,"8":8,"9" : 9,"T" : 10, "J":11,"Q"  :12 ,"K" :13, "A":14}
    print(handa,handb)
    if handa['constrank']  < handb['constrank']: return True
    if handa['constrank']  > handb['constrank']: return False

    for i in range(0,5):
        #if len(handa['cards']) !=5:
          #  print("LängeA", handa['cards'])
        #if len(handb['cards']) !=5:
          #  print("LängeB", handa['cards'])
        a = handa['cards'][i]
        b = handb['cards'][i]
        #print(a,b)
        if cv[a] == cv[b]: continue
        if cv[a] < cv[b]: return True
        if cv[a] > cv[b]: return False


def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()

lines = load("input.txt")
hands = []
for line in lines:
    lhand = {}
    lparts = line.split()
    lhand['cards'] = lparts[0]
    
    lhand['bid'] = int(lparts[1])
    hands.append(lhand)


for hand in hands:
    #getconst(hand['cards'])
    hand['const'], hand['constrank'], hand['cards'] = getconst(hand['cards'])
    if len(hand['cards']) != 5:
        print("Anzahl Karten ungülti!")

#print(hands)

print(json.dumps(hands, indent=4))

for au_idx in range(1,len(hands)):
    for in_idx in range(au_idx,len(hands)):
        #print(au_idx,in_idx)
        if compareconst(hands[in_idx], hands[au_idx-1]):
            help = hands[au_idx-1]
            hands[au_idx-1] = hands[in_idx]
            hands[in_idx] = help

#print(json.dumps(hands, indent=4))

total_winnings  = 0
for i in range(0,len(hands)):
    hands[i]['winnings'] = hands[i]['bid'] * (i+1)
    total_winnings += hands[i]['winnings']
    print(f"{hands[i]['cards']}, {hands[i]['const']} Rank : {i+1}, {hands[i]['bid']},{hands[i]['winnings']},{total_winnings}")



print(total_winnings)    