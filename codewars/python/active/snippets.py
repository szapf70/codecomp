import math

def ellipse(a, b):
    a = math.pi * a * b
    
    p = a+b
    print(p)
    p *= 2
    print(p)
    p = 3/p
    print(p)
    t = a*b
    print(p,t)
    t = t**0.5
    print(p,t)
    p = p-t
    print(p)
    p *= math.pi
        

    return f"Area: {round(a,1)}, perimeter {round(p,1)}"

ellipse(5,2)