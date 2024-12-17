# https://www.codewars.com/kata/596c26187bd547f3a6000050/train/python
# Simple Fun #342: Buy Newspaper




def buy_newspaper(s1,s2):
    s1c = {}
    s2c = {}
    
    for l in 'abcdefghijklmnopqrstuvwxyz':
        l1 = s1.count(l)
        l2 = s2.count(l)
        if not l1 and l2:
            return -1
        if l1:
            s1c[l] = s1c.get(l,0) + 1
        if l2:
            s2c[l] = s2c.get(l,0) + 1   

    how_many = 0

    for l in s2c:
        _how = s2c[l] // s1c[l] + 1
        if _how > how_many:
            how_many = _how

    return how_many


print(buy_newspaper("abc","bcac"),2)
print(buy_newspaper("abc","xyz"),-1)
print(buy_newspaper("abc","abcabc"),2)
print(buy_newspaper("abc","abccba"),4)
print(buy_newspaper("abc","aaaaaa"),6)