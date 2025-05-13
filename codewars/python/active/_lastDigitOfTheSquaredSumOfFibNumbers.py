# https://www.codewars.com/kata/62ea53ae888e170058f00ddc/train/python
# Last digit of the squared sum of Fibonacci numbers


f = [0,1]
sf = [0,1]

def fibonacci_squared_sum(n):
    while len(f) <= 60:
        f.append(f[-1] + f[-2])
        sf.append(f[-1]**2)
    sf60 = sum(sf)
    print(f,sf,sf60)
    d,r = divmod(n+1,60)
    res = d * sf60 + sum(sf[:r])
    return res%10

print(fibonacci_squared_sum(7))
        