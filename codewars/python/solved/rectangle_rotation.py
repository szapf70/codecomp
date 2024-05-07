# https://www.codewars.com/kata/5886e082a836a691340000c3/train/python

def rectangle_rotation_old(a, b):
    d = int(max(a,b)/2)+1
    c = 0
    af = (b/2)*(2**.5)
    afn = -(b/2)*(2**.5)
    bf = (a/2)*(2**.5)
    bfn = -(a/2)*(2**.5)
    for x,y in [(a,b) for a in range(-d,d+1) for b in range(-d,d+1)]:
        if af+x >= y >= afn+x and bf-x >= y >= bfn-x:
            c += 1
    return c

def rectangle_rotation(a, b):
    def rnger(u,l):
        lu = 0
        ll = 0
        if u >= 0 : lu = int(u)
        else: lu = int(u)-1
        if l >= 0 : ll = int(l)+1
        else: ll = int(l)
        return lu,ll
    
    d = int(max(a,b)/2)+2
    c = 0
    af = (b/2)*(2**.5)
    afn = -(b/2)*(2**.5)
    bf = (a/2)*(2**.5)
    bfn = -(a/2)*(2**.5)
    for x in range(-d,d+1):
        upper = min(af+x,bf-x)
        lower = max(afn+x, bfn-x)
        if upper > lower:
            upper, lower = rnger(upper,lower)
            r = (upper-lower)+1
            c += r
            print(x,upper,lower,r,c)
    return c



print(rectangle_rotation(8,6))