# https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python
# Fibonacci, Tribonacci and friends

def xbonacci(signature, n):
    if n <= len(signature):
        return signature[-n:]
    osl = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[len(signature)-osl:]))
    return signature    
        
print(xbonacci([0,0,0,0,1],10))        
        