# https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python
# Last digit of a large number

def last_digit(n1, n2):
    seqs = { "0" : [0],
             "1" : [1],
             "2" : [2,4,8,6],
             "3" : [3,9,7,1],
             "4" : [4,6],
             "5" : [5],
             "6" : [6],
             "7" : [7,9,3,1],
             "8" : [8,4,2,6],
             "9" : [9,1]}
    
    l1 = str(n1)[-1:]
    if l1 in '0156' or n1 == 1: return seqs[l1][0]
    return seqs[l1][n2%(len(seqs[l1]))-1]

print(last_digit(3715290469715693021198967285016729344580685479654510946723,68819615221552997273737174557165657483427362207517952651), " sollte 7")
#print(2**200)
#print(2**300)
#print(6**(2**300))
#print((2**200)**(2**300))


"""

You may assume that the input will always be valid.

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
"""