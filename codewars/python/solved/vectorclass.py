# https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4/train/python
# Vector class


from typing import Any


class Vector:
    vector = None
    def __init__(self, vec):
        self.vector = vec
        return

    def __str__(self):
        return f"({','.join([str(v) for v in self.vector])})"

    def add(self, other):
        if len(self.vector) != len(other.vector):
            raise Exception("Wrong size!")
        return Vector([self.vector[i]+ other.vector[i] for i in range(len(self.vector))])

    def subtract(self, other):
        if len(self.vector) != len(other.vector):
            raise Exception("Wrong size!")
        return Vector([self.vector[i]- other.vector[i] for i in range(len(self.vector))])

    def dot(self, other):
        if len(self.vector) != len(other.vector):
            raise Exception("Wrong size!")
        dot = 0
        for i in range(len(self.vector)):
            dot += self.vector[i] * other.vector[i]
        return dot    
    
    def norm(self):
        norm = 0
        for i in range(len(self.vector)):
            norm += self.vector[i]**2
        return norm    

    def equals(self, other):
        if len(self.vector) != len(other.vector):
            raise Exception("Wrong size!")
        for i in range(len(self.vector)):
            if self.vector[i] != other.vector[i]:
                return False
            return True


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
print(a.add(b))
print(a.subtract(b))
print(a.dot(b))
print(a.norm())

"""Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.

"""