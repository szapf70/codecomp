# https://www.codewars.com/kata/55217af7ecb43366f8000f76/train/python
# Mysterious function

def get_num(num):
    nstr = str(n)
    q = 0
    for d in nstr:
        q += int(d)
    return q                
    



nums = [300,90783,123321,89282350306,3479283469]

for n in nums:
    print(get_num(n))