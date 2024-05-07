from collections import defaultdict
import json
import sys

def getwealth(cards):
    lcnt = defaultdict(int)
    for card in cards:
        lcnt[card] += 1
    picture = "".join(sorted(list(map(str,lcnt.values())),reverse=True))
    picscores = {"5" : 7,"41" : 6,"32" : 5, "311" : 4, "221" : 3, "2111" : 2, "11111"  :1}
    score = 0
    cv = {"J":1,"2" : 2, "3" : 3,"4" :4, "5" :5,"6" :6,"7":7,"8":8,"9" : 9, "T" : 10, "Q"  :12 ,"K" :13, "A":14}
    powers = [100000000 ,1000000, 10000,100,1]
    for i in range(0,5):
        j = cv[cards[i]]
        score += j*powers[i]
    return cards,picscores[picture], score    



def jokerizer(cards):
    if not 'J' in cards: return cards
    perms = []
    for j in "AKQT98765432":
        lcards = cards.replace('J', j)
        perms.append(getwealth(lcards))        
    
    for au_idx in range(1,len(perms)):
        for in_idx in range(au_idx, len(perms)):
            if perms[au_idx-1][1] > perms[in_idx][1]: continue
            if perms[au_idx-1][1] < perms[in_idx][1]: 
                help = perms[au_idx-1]
                perms[au_idx-1] = perms[in_idx]
                perms[in_idx] = help
                continue
            if perms[au_idx-1][2] > perms[in_idx][2]: continue
            if perms[au_idx-1][2] < perms[in_idx][2]: 
                help = perms[au_idx-1]
                perms[au_idx-1] = perms[in_idx]
                perms[in_idx] = help
    return perms[0][0]        
    
    
    
    
    



    #conste, constemap  = getconste(cards)
    



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


##print(hands)
for hand in hands:
    hand['jcards'] = jokerizer(hand['cards'])
###print(hands)

for hand in hands:
    _, picscore, _  = getwealth(hand['jcards'])
    _, _ , score = getwealth(hand['cards'])
    hand['picscore'] = picscore
    hand['score'] = score



#print(hands)
for au_idx in range(1,len(hands)):
    for in_idx in range(au_idx, len(hands)):
        if hands[au_idx-1]['picscore'] < hands[in_idx]['picscore']: continue
        if hands[au_idx-1]['picscore'] > hands[in_idx]['picscore']: 
            help = hands[au_idx-1]
            hands[au_idx-1] = hands[in_idx]
            hands[in_idx] = help
            continue
        if hands[au_idx-1]['score'] < hands[in_idx]['score']: continue
        if hands[au_idx-1]['score'] > hands[in_idx]['score']: 
            help = hands[au_idx-1]
            hands[au_idx-1] = hands[in_idx]
            hands[in_idx] = help


total_winnings  = 0
for i in range(0,len(hands)):
    if i % 25 == 0: print(i,"\r")
    total_winnings += hands[i]['bid'] * (i+1)

 
print(json.dumps(hands, indent=4))
print(total_winnings)
 


sys.exit()
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