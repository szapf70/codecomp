# https://www.codewars.com/kata/53ad69892a27079b34000bd9/train/python
# Ackermann Function

def Ackermann(m, n):
    if m == 0:
        return n + 1
    
    if m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    
    if m > 0 and n > 0:
        return Ackermann(m-1,Ackermann(m, n-1))


print(Ackermann(4,0))