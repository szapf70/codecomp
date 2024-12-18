# https://www.codewars.com/kata/5476f4ca03810c0fc0000098/train/python
# Calculate the function f(x) for a simple linear sequence (Easy)

from itertools import pairwise

def get_function(seq):
    d = set([a-b for a,b in pairwise(seq)])
    if 1 < len(set(seq)) < 5 or len(d) > 1:
        return "Non-linear sequence"
    x = seq[1] - seq[0]
    if x != 0 :
        bstr = f"f(x) = {str(x)}x"
    else:
        bstr = f"f(x) = {seq[0]}"
        return bstr
    if abs(x) == 1:
        bstr = bstr.replace('1', '')
    if seq[0] != 0:
        if seq[0] > 0:
            bstr += f" + {str(seq[0])}"
        else:
            bstr += f" - {str(abs(seq[0]))}"
    return bstr    



seqs = [([3,3,3,3,3], "f(x) = 3"),([0, 1, 2, 3, 4],"f(x) = x"),([0, 3, 6, 9, 12],"f(x) = 3x"),([1, 4, 7, 10, 13],"f(x) = 3x + 1"), ([3,-1, -5 , -9,-13], "f(x) = -4x + 3")]

for s,r in seqs:
    print(f"Sequence {s} : Result {get_function(s)} : Expected {r}")