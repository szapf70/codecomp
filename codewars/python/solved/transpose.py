# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/python
# Matrix Transpose

def transpose(matrix):
    res = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))] 

    for i in range(len(matrix)):
        for y in range(len(matrix[0])):
            res[y][i] = matrix[i][y]

    return res



print(transpose([[1, 2, 3]]))
print([[1], [2], [3]])

print(transpose([[1, 2], [5, 6], [7, 8]]))
print([[1, 5, 7], [2, 6, 8]])

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print([[1, 4, 7], [2, 5, 8], [3, 6, 9]])


