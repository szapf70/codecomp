# https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/train/python
# Reversing a Process

import re

def decode(r):
    n = int(re.findall(r'[\d.]+', r)[0])
    return n


print(decode("1273409kuqhkoynvvknsdwljantzkpnmfgf"))