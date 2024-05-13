# https://www.codewars.com/kata/523d2e964680d1f749000135/train/python
# Interleaving Arrays

def interleave(*args):
    if len(args) == 1 and args[0] == []: return []
    res = []
    # Get Maxlen
    ml = max([len(arg) for arg in args])

    for _ in range(ml):
        for ai in range(len(args)):
            if args[ai] == []: res.append(None)
            else: res.append(args[ai].pop(0))
    return res

args = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

print(interleave(*args))


