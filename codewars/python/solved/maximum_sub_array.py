# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
# Maximum subarray sum

import numpy as np

def max_sequence_old(arr):
    if arr == []: return 0
    a = np.array(arr)
    if np.all(a < 0): return 0
    max = -100_000_000
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)+1):
            v = np.sum(a[i:j])
            if v > max: max = v
    return max

def max_sequence_to_slow(arr):
    if arr == [] or max(arr) < 0 : return 0
    m = -100_000_000
    s = None
    l = len(arr)
    for i in range(0,l):
        s = arr[i]
        if s > m: m = s
        for j in range(i+1,l):
            s += arr[j]
            if s > m: m = s
    return m

# Kadane Algorithmus

def max_sequence_kadane(arr):
    m1 = 0
    m2 = 0
    for i in arr:
        m1 = max(i, m1 + i)
        m2 = max(m2, m1)
    return m2

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
            
            



