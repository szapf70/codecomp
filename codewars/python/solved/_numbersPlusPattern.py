# https://www.codewars.com/kata/563cb92e0996a4ac0b000042/train/python
# Numbers' Plus Pattern


def stairs(n):
    _org = ['1','2','3','4','5','6','7','8','9','0']
    _stairs = []
    _size = 4*n-1    
    for c in range(1,n+1):
        _w = _org * (c//10) + _org[:c%10]
        print(_w)
        _stairs.append(" ".join(_w.copy()+_w.copy()[::-1]).rjust(_size))
    return "\n".join(_stairs)

def pattern(n):
    _lines = []
    for c in range(1,n):
        _lines.append(str(c%10).rjust(n))
    _org = ['1','2','3','4','5','6','7','8','9','0']
    _w = "".join(_org * ((n-1)//10) + _org[:(n-1)%10])
    _lines.append(_w + str(n%10) +_w[::-1])
    for c in range(n-1,0,-1):
        _lines.append(str(c%10).rjust(n))

    return "\n".join(_lines) + "\n"

print(pattern(3))