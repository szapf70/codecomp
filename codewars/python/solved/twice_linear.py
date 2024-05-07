from collections import deque

def dbl_linear(n):
    u = set()
    u2 = deque()
    u.add(1)
    u2.append(1)
    while len(u) < n*5:
        i = u2.popleft()
        #print(u,u2)
        u.add(i*2+1)
        u.add(i*3+1)
        u2.append(i*2+1)
        u2.append(i*3+1)

    res = sorted(u)
    #print(res)
    return res[n]

print(dbl_linear(100))

"""
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u 
(so, there are no duplicates).

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency



"""