# https://www.codewars.com/kata/534ffb35edb1241eda0015fe/train/python
# Blackjack Scorer

def score_hand(cards):
    crds = { '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7 , '8' : 8, '9' : 9,
             'J' : 10, 'Q' : 10, 'K' : 10}
    ace = 0
       
    ace = cards.count("A")
    cards = [c for c in cards if c != "A"]
    fsum = sum([crds[c] for c in cards])
    
    if ace == 0:
        return fsum
    
    sl = [fsum + ace]
    
    for a in range(1,1+ace):
        sl.append(sl[0] + a*10)

    sc = [s for s in sl if s <= 21]
    l = [s for s in sl if s > 21]

    if sc:
        return sc[-1]
    else:
        return l[0]
     
    


print(score_hand(['2','3']), 5)
print(score_hand(['4','5','6']), 15)
print(score_hand(['7','7','8']), 22)
print(score_hand(['7','8','A','A','A']), 22)