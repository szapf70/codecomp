# https://www.codewars.com/kata/5476f4ca03810c0fc0000098/train/python
# Calculate the function f(x) for a simple linear sequence (Easy)

def get_function(sequence):
    print(sequence)
    if len(set(sequence)) < 5 or len(set()):
        return "Non-linear sequence"
    x = sequence[1] - sequence[0]
    bstr = f"f(x) = {str(x)}x"
    if abs(x) == 1:
        bstr = bstr.replace('1', '')
    if sequence[0] != 0:
        if sequence[0] > 0:
            bstr += f" + {str(sequence[0])}"
        else:
            bstr += f" - {str(abs(sequence[0]))}"
    return bstr    

seqs = [([0, 1, 2, 3, 4],"f(x) = x"),([0, 3, 6, 9, 12],"f(x) = 3x"),([1, 4, 7, 10, 13],"f(x) = 3x + 1"), ([3,-1, -5 , -9,-13], "f(x) = -4x + 3")]

for s,r in seqs:
    print(f"Sequence {s} : Result {get_function(s)} : Expected {r}")