from functools import cmp_to_key

def compare(a, b):
    if len(a) < len(b): return -1
    if len(a) > len(b): return 1

    if a[0] > b[0]: return -1
    if a[0] < b[0]: return 1

    if a[2] > b[2]: return -1
    if a[2] < b[2]: return 1
    return 0

def mix(s1, s2):
    res = []
    for l in 'abcdefghijklmnopqrstuvwxyz':
        c1 = s1.count(l)
        c2 = s2.count(l)
        if max(c1,c2) > 1:
            lbuf = ""
            if c1 > c2: lbuf = "1:"
            if c2 > c1: lbuf = "2:"
            if c1 == c2: lbuf = "=:"
            lbuf += l * max(c1,c2) 
            res.append(lbuf)   
    res = sorted(res, key=cmp_to_key(compare),reverse = True)

    return "/".join(res)


s1 = "Sadus:cpms>orqn3zecwGvnznSgacs"
s2 = "MynwdKizfd$lvse+gnbaGydxyXzayp"

##s1 = "my&friend&Paul has heavy hats! &"
#s2 = "my friend John has many many friends &"
print(mix(s1, s2)) # --> 

print("2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz")

#print("2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")

#print(sorted(['2:aa','3:bbb','5:mmmmm','3:ccc'],reverse = True))




"""
s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""