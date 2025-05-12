# https://www.codewars.com/kata/59e66e48fc3c499ec5000103/train/python
# Array combinations

def solve(arr):
    res = 1
    arr = list(map(set, arr))
    for s in arr:
        res *= len(s)
    
    return res

print(solve([[1,2],[4],[5,6]]),4)
print(solve([[1,2],[4,5],[5,6,6]]),8)
print(solve([[1,2],[4,4],[5,6,6]]),4)
print(solve([[1,2],[3,4],[5,6]]),8)
print(solve([[1,2,3],[3,4,6,6,7],[8,9,10,12,5,6]]),72)