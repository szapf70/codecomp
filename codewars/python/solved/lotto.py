# https://www.codewars.com/kata/57a98e8172292d977b000079
# LOTTO 6 aus 49 - 6 of 49


import random

def number_generator():
    res = sorted(random.sample(range(1,50), 6))
    res.append(random.randint(0,9))
    return res

def check_for_winning_category(your_numbers, winning_numbers):
    res = [0,61,60,51,50,41,40,31,30,21]
    s = int(your_numbers.pop(-1) == winning_numbers.pop(-1))
    s += 10*len(set(your_numbers).intersection(set(winning_numbers)))
    if s in res: return res.index(s)
    return -1

print(number_generator())
print(check_for_winning_category([1, 2, 3, 34, 35, 39, 1 ], [1, 2, 3, 4, 5, 6, 7 ]))

"""
        test.assert_equals(check_for_winning_category([1, 2, 3, 4, 5, 6, 7 ], [1, 2, 3, 4, 5, 6, 7 ]), 1)
        test.assert_equals(check_for_winning_category([1, 2, 3, 4, 5, 6, 0 ], [1, 2, 3, 4, 5, 6, 7 ]), 2)
        test.assert_equals(check_for_winning_category([1, 2, 3, 34, 35, 39, 1 ], [1, 2, 3, 4, 5, 6, 7 ]), 8)
        test.assert_equals(check_for_winning_category([11, 12, 13, 34, 35, 39, 1 ], [1, 2, 3, 4, 5, 6, 7 ]), -1)
        test.assert_equals(check_for_winning_category([1, 12, 13, 34, 35, 39, 1 ], [1, 2, 3, 4, 5, 6, 1 ]), -1)
        test.assert_equals(check_for_winning_category([8, 25, 32, 40, 41, 48, 3], [8, 30, 36, 38, 40, 48, 5]), 8)

DESCRIPTION:
In Germany we have "LOTTO 6 aus 49". That means that 6 of 49 numbers are drawn as winning combination.
There is also a "Superzahl", an additional number, which can increase your winning category.

In this kata you have to write two methods.

def number_generator():

def check_for_winning_category(your_numbers, winning_numbers):
The first method is for drawing the lottery numbers.
You have to create an array with 7 random numbers. 6 from these are from 1 - 49.
Of course every number may only occur once.
And the 7th number is the "Superzahl". A number from 0 - 9. This number is independent from the first six numbers.
The first 6 numbers have to be in ascending order.

A result could be:
4, 9, 17, 22, 25, 35, 0
Or:
4, 18, 22, 34, 41, 44, 4

The second method should check a given number against the winning combination and have to return the winning category:

1  - 6 numbers and Superzahl match
2  - 6 numbers match
3  - 5 numbers and Superzahl match
4  - 5 numbers match
5  - 4 numbers and Superzahl match
6  - 4 numbers match
7  - 3 numbers and Superzahl match
8  - 3 numbers match
9  - 2 numbers and Superzahl match
-1 - if the numbers do not match any of the rules above


Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
"""