# https://www.codewars.com/kata/58f6000bc0ec6451960000fd/train/python
# Selective Array Reversing

def sel_reverse(arr,l):
    print(arr,l)
    res = []
    while l <= len(arr):
        res.extend(arr[:l])
        l = arr[l:]
    res.extens(arr)
    return res

print(sel_reverse([2,4,6,8,10,12,14,16], 3))
