# https://www.codewars.com/kata/54ce4c6804fcc440a1000ecb/train/python
# Burrows-Wheeler-Transformation

def encode(s):
    l= []
    ls = s
    for _ in range(len(s)):
        l.append(ls)
        ls = ls[-1]+ls[:-1]
    l = sorted(l)
    oidx = l.index(ls)     
    res = ""
    for w in l:
        res += w[-1]
    return res,oidx

def decode(s, n):
    buf = [""] * len(s)
    for _ in range(len(s)):
        for i in range(len(s)):
            buf[i] = s[i]+buf[i]
        buf = sorted(buf)
    return buf[n]

print(encode("bananabar"))
print(decode("nnbbraaaa",4))

"""

"""