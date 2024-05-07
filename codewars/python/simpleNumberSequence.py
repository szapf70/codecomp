# https://www.codewars.com/kata/5a28cf591f7f7019a80000de/train/python
# Simple number sequence

import itertools

def listValid(l):
    nl = [int(ns) for ns in l]
    nb = [int(b)-int(a) for a,b in itertools.pairwise(nl)]
    return set(nb) == {1,2} and nb.count(1) == len(nb)-1 and nb.count(2) == 1

def missing(s):
    



    print(listValid(s))
    



    
missing(["1","2","3","5","6"])
missing(["111","112","113","114","115"])
missing(["1000","1002","1004","1006"])
missing(["1","2","3","5","6"])
