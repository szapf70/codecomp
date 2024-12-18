# https://www.codewars.com/kata/635fc0497dadea0030cb7936/train/python
# Same matrix (2 * 2)


def norm_matrice(matrice):
    lm = tuple(matrice)
    res = [lm]
    for _ in range(3):
        at = res[-1]
        res.append((at[2],at[0],at[3],at[1]))
    res = sorted(res)
    return res[0] 

def count_different_matrices(matrices):
    s = set()
    for m in matrices:
        s.add(norm_matrice(m))

    return len(s)
    
print(count_different_matrices([[1, 2, 2, 1],
                [1, 1, 2, 2],
                [2, 1, 1, 2],
                [2, 1, 2, 1],
                [1, 2, 1, 2]]))    
