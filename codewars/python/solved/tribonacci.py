# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
# Tribonacci Sequence

def tribonacci(signature, n):
    print(signature,n)
    if n == 0 : return []
    if 1 <= n <= 3:
        return signature[n-1:n]
    i = 3
    while i < n:
        signature.append(signature[i-1] + signature[i-2] + signature[i-3])
        i += 1
    return list(signature)    
        

