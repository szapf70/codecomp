# https://www.codewars.com/kata/56a1c63f3bc6827e13000006/train/python
# How many are smaller than me II?

import numpy as np

def smaller(arr):
    arr = np.array(arr)
    rarr = np.zeros(len(arr),dtype=np.int64)

    for n in range(0,len(arr)):
        rarr[n] = np.sum(arr[n:] < arr[n])

    return list(rarr) 


print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
#print(smaller([5, 4, 7, 9, 2, -6, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])

"""
clist = ["count"]
df = pd.DataFrame(0, index=np.arange(7), columns=clist) 

print(df["count"][0]) 
df['count'][0] = 1
df['count'][1] = 2
print(sum(df['count'][0:2]))
"""