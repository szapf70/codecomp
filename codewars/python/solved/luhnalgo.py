# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2/train/python
# Validate Credit Card Number

def validate(n):
    nums = [int(d)*(1+i%2) for i,d in enumerate(str(n)[::-1])][::-1]
    num = sum([n - 9 if n > 9 else n for n in nums])
    return not num%10


print(validate(2121))
print(validate(12345))
print(validate(891))



