# https://www.codewars.com/kata/55a5c82cd8e9baa49000004c/train/python
# Count the divisible numbers

def divisible_count(x, y, k):
    lx = x if x%k == 0 else (int(x//k)+1)*k
    ly = y if y%k == 0 else (int(y//k))*k
    return (ly-lx)//k+1




print(divisible_count(6,11,2))
print(divisible_count(11,345,17))


