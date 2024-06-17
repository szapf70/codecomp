# https://www.codewars.com/kata/562e6df5cf2d3908ad00019e
# Don't Drink the Water

import itertools

def separate_liquids(glass):
    pre = list(itertools.chain(*glass))
    prec = len(glass[0])
    t = []
    for l in ['O','A','W','H']:
        t.extend([l] * pre.count(l))
    res = []
    while t:
        res.append(t[:prec])
        t = t[prec:]
    return res
