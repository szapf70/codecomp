# https://www.codewars.com/kata/5b1b27c8f60e99a467000041/train/python
# Anagram difference

def anagram_difference(w1, w2):
    l1 = sorted(list(w1))
    l2 = sorted(list(w2))
    res = 0

    for l in set(l1+l2):
        c1 = l1.count(l)
        c2 = l2.count(l)
        res += abs(c1-c2) 


    return res

print(anagram_difference('codewars', 'hackerrank'))

