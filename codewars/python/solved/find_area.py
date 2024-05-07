# https://www.codewars.com/kata/59b166f0a35510270800018d/train/python
# Find an area

from itertools import pairwise

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        
    def __str__(self):
        return f"{self.X}/{self.Y}"


def find_area(points):
    area = 0
    for a,b in pairwise(points):
        if a.Y > 0 and b.Y > 0:
            area += abs(b.X-a.X) * min(b.Y,a.Y)
        area += (abs(b.X-a.X) * (max(b.Y,a.Y)-min(a.Y,b.Y)))/2
    return area


print(find_area([Point(-3, 0), Point(-1, 4), Point(3, 2)]))
