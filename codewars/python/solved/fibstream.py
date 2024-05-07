# https://www.codewars.com/kata/55695bc4f75bbaea5100016b/train/python 
# Fibonacci Streaming

def all_fibonacci_numbers():
    a,b = 0,1
    while True:
        a,b = b, a+b
        yield a
        
fib = all_fibonacci_numbers()        
for _ in range(30):
    print(next(fib))        