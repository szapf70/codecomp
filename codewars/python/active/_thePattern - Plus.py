# https://www.codewars.com/kata/5589ad588ee1db3f5e00005a/train/python
# Complete The Pattern #11 - Plus



def pattern(n):
    if n < 1:
        return ""
    _lines = []
    for c in range(1,n):
        _lines.append(" " * (n-1) + (str(c%10) * n) + " " * (n-1))
    _org = ['1','2','3','4','5','6','7','8','9','0']
    _w = "".join(_org * ((n-1)//10) + _org[:(n-1)%10])
    for _ in range(n):
        _lines.append(_w + str(n%10) * n +_w[::-1])
    for c in range(n-1,0,-1):
        _lines.append(" " * (n-1) + (str(c%10) * n) + " " * (n-1))

    return "\n".join(_lines)

print(pattern(5))