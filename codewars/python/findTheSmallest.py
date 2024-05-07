# https://www.codewars.com/kata/573992c724fc289553000e95/train/python
# Find the smallest

def smallest(n):
    res = [[n, 0, 0]]
    nums = list(str(n))
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            lnums = nums
            temp = lnums[i]
            lnums[i] = lnums[j]
            lnums[j] = temp
            lres = [int("".join(lnums)), j,i]
            res.append(lres)
    res = sorted(res)
    return res[0]


print(smallest(261235))        
print(smallest(209917))        
print(smallest(285365))        
print(smallest(269045))        
print(smallest(296837))        
            
    