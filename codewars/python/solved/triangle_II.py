# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    s = sorted([a,b,c])
    if s[2] >= s[0]+s[1] : return 0
    if s[0]**2 + s[1]**2 == s[2]**2 : return 2
    if s[2]**2 < s[0]**2 + s[1]**2 : return 1
    return 3



print(triangle_type(7, 3, 2))#, 0) # Not triangle
print(triangle_type(2, 4, 6))#, 0) # Not triangle
print(triangle_type(8, 5, 7))#, 1) # Acute
print(triangle_type(3, 4, 5))#, 2) # Right
print(triangle_type(7, 12, 8))#, 3) # Obtuse#
