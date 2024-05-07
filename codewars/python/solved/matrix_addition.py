# https://www.codewars.com/kata/526233aefd4764272800036f/train/python
# Matrix Addition

def matrix_addition(a, b):
    c = []
    for i in range(0,len(a)):
        c.append([])
        for y in range(0,len(a[0])):
            c[-1].append(a[i][y] + b[i][y])
    return c



#

print(matrix_addition([[1, 2, 3], [3, 2, 1], [1, 1, 1]],[[2, 2, 1], [3, 2, 3], [1, 1, 3]]))