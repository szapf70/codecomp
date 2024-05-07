# https://www.codewars.com/kata/52549d3e19453df56f0000fe/train/python
# Fibonacci Reloaded


def fib(n):
    f = [0,1]
    if abs(n) < 2: return f[abs(n)]
    i = 1
    while i < abs(n):
        f.append(f[-2] + f[-1])
        i += 1
    return f[-1] if n >= 0 else f[-1]*-1  
        
        
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(-6))
