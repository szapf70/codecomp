# https://www.codewars.com/kata/5921c0bc6b8f072e840000c0/train/python
# Sequence classifier

from itertools import pairwise


def sequence_classifier(arr):
    lres = [b - a for a,b in pairwise(arr)]
    # check 5 (constant)
    if all([n == 0 for n in lres]):
        return 5
    # 1 (strict inc
    if all([n > 0 for n in lres]):
        return 1
    # 2 not dec
    if all([n >= 0 for n in lres]):
        return 2
    # 1 (strict inc
    if all([n < 0 for n in lres]):
        return 3
    # 2 not dec
    if all([n <= 0 for n in lres]):
        return 4
    return 0



print(sequence_classifier([3,5,8,8,14,14]))