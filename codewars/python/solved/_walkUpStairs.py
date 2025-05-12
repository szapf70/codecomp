# https://www.codewars.com/kata/566c3f5b9de85fdd0e000026/train/python
# Walk-up Stairs



def stairs(n):
    _org = ['1','2','3','4','5','6','7','8','9','0']
    _stairs = []
    _size = 4*n-1    
    for c in range(1,n+1):
        _w = _org * (c//10) + _org[:c%10]
        print(_w)
        _stairs.append(" ".join(_w.copy()+_w.copy()[::-1]).rjust(_size))
    return "\n".join(_stairs)





print(stairs(3))