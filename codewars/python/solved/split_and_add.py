# https://www.codewars.com/kata/5946a0a64a2c5b596500019a/train/python
# Split and then add both sides of an array together.

def split_and_add(numbers, n):
    nums = numbers
    while n > 0:
        n1 = nums
        n2 = nums[int(len(n1)/2):]
        del n1[int(len(n1)/2):]
        if len(n1) < len(n2):
            n1.insert(0,0)  
        nums = [n1[i]+n2[i] for i in range(len(n1))]
        n -= 1
    return nums


print(split_and_add([4, 2, 5, 3, 2, 5, 7], 2))
print(split_and_add([1,2,3,4,5], 2))
print(split_and_add([1,2,3,4,5], 3))