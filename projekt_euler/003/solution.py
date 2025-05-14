import sympy

#s = 600851475143
s = 13195
a = s
p = []

while a < s:
    a = sympy.prevprime(a)
    print("Testing: " + str(a))
    if s%a == 0:
        p.append(a)

print(p)        