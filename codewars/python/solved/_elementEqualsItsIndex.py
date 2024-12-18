# https://www.codewars.com/kata/5b7176768adeae9bc9000056/train/python
# Element equals its index


def index_equals_value(arr):
    if arr[0] > 0 or arr[-1] < len(arr)-1:
        return -1
    
    left = 0
    right = len(arr) - 1

    while right - left > 5:
        act = left + (right-left)//2
        if arr[act] == act:
            while arr[act-1] == act-1:
                act -= 1
            return act
        if arr[act] > act:
            right = act
            continue
        if arr[act] < act:
            left = act

    for i in range(left, right+1):
        if arr[i] > i:
            return -1
        if arr[i] == i:
            return i
    return -1   







jobs = [(-3,0,1,3,10),(-5, 1, 2, 3, 4, 5, 7, 10, 15),(9,10,11,12,13,14),(0,)]

for job in jobs:
    print(index_equals_value(job))    