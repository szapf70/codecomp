# https://www.codewars.com/kata/58bf97cde4a5edfd4f00008d/train/python
# Simple Fun #189: Plant Doubling

def plant_doubling(n):
    r = 0
    while n:
        rt = n**0.5
        r += int(rt)
        n -= int(rt**2)
    return r    
    
    
print(plant_doubling(536870911))    



