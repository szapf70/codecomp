# https://www.codewars.com/kata/62ea53ae888e170058f00ddc/train/python
# Last digit of the squared sum of Fibonacci numbers


def fib_list():
    f = [0,1]
    sf = [0,1]
    for i in range(240):
        f.append(f[-1]+f[-2])
        sf.append(f[-1]**2)
    print([str(_f)[-1] for _f in f[1:61]])
    print([str(_f)[-1] for _f in f[61:121]])




def fib_last(n):
    a,b = 0,1
    s = 0
    for i in range(n):
        s += b**2
        a,b = b, a+b
    return s,str(s)[-1]


print(fib_list())
        