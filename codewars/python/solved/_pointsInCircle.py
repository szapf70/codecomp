# https://www.codewars.com/kata/5b55c49d4a317adff500015f/train/python
# Points in the circle

import math


def points(n):
    c = 0
    for x in range(0, n+1):
        for y in range(1, n+1):
            if x**2 + y**2 <= n**2:
                count += 1
    return c*4 + 1


# Beispielnutzung
radius = 5
print(f"Die Anzahl der Gitterpunkte innerhalb des Kreises mit Radius {radius} ist {count_lattice_points(radius)}.")
print(f"Die Anzahl der Gitterpunkte innerhalb des Kreises mit Radius {radius} ist {cpfast(radius)}.")