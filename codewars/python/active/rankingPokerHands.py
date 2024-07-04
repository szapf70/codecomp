# https://www.codewars.com/kata/5739174624fc28e188000465/train/python
# Ranking Poker Hands

class PokerHand:
    STR_PAT = "A23456789TJQKA"
    RKI = ["1112","122","113","23","14"]
    RESULT = ["Loss", "Tie", "Win"]
    FLAGS = set()
    def __init__(self, hand):
        hand.split()
        self.cards = []
        vcnt = {}
        scnt = {}
        vals = []
        suits = []
        
        for cards in hand.split():
            v,s = cards[0], cards[1]
            self.cards.append((v, s))
            # Werte, und Farbensignaturen ermitteln
            vcnt[v] = vcnt.get(v,0) + 1
            scnt[s] = scnt.get(s,0) + 1
            vals.append(v)
            suits.append(s)
        self.value_sig = "".join([str(c) for c in sorted(vcnt.values())])
        # strasse?
        if self.value_sig == "11111":
            pass    
        self.suit_sig = "".join([str(c) for c in sorted(scnt.values())])
        self.vals = sorted(vals)
        self.suits = sorted(suits)
        print(self.vals,self.value_sig,self.suits,self.suit_sig)
        
    def compare_with(self, other):
        pass
    
ph = PokerHand("2S 2H 4H 5S 4C")




"""

        run_test("Highest straight flush wins",        "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
        run_test("Straight flush wins of 4 of a kind", "Win",  "2H 3H 4H 5H 6H", "AS AD AC AH JD")
        run_test("Highest 4 of a kind wins",           "Win",  "AS AH 2H AD AC", "JS JD JC JH 3D")
        run_test("4 Of a kind wins of full house",     "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
        run_test("Full house wins of flush",           "Win",  "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
        run_test("Highest flush wins",                 "Win",  "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")
        run_test("Flush wins of straight",             "Win",  "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")
        run_test("Equal straight is tie", 	  	       "Tie",  "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")
        run_test("Straight wins of three of a kind",   "Win",  "2S 3H 4H 5S AD", "AH AC 5H 6H AS")
        run_test("3 Of a kind wins of two pair",       "Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")
        run_test("2 Pair wins of pair",                "Win",  "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")
        run_test("Highest pair wins",                  "Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")
        run_test("Pair wins of nothing",               "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
        run_test("Highest card loses",                 "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
        run_test("Highest card wins",                  "Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")
        run_test("Equal cards is tie",		           "Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")


A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also online. Can you help them by writing an algorithm that can rank poker hands?

Task
Create a poker hand that has a method to compare itself to another poker hand:

compare_with(self, other_hand)
A poker hand has a constructor that accepts a string containing 5 cards:

PokerHand("KS 2H 5C JD TD")
The characteristics of the string of cards are:

Each card consists of two characters, where
The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
A space is used as card separator between cards
The result of your poker hand compare can be one of these 3 options:

[ "Win", "Tie", "Loss" ]
Notes
Apply the Texas Hold'em rules for ranking the cards.
Low aces are valid in this kata.
There is no ranking for the suits.
If you finished this kata, you might want to continue with Sortable Poker Hands
"""    