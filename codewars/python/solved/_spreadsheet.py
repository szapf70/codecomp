# https://www.codewars.com/kata/58b38f24c723bf6b660000d8/train/python
# Simple Fun #167: Spreadsheet

import re

def intToLetter(i):
    col = ""
    while i > 0:
        i -= 1
        col = chr(i%26+ord('A')) + col
        i//=26
    return col

def letterToInt(l):
    col = 0
    for i, c in enumerate(l):
        col = col * 26 + (ord(c.upper()) - ord('A') + 1)
    return col

#print(letterToInt("A"))
#print(letterToInt("AA"))
#print(letterToInt("CRXO"))

def spreadsheet(s):
    nums = re.findall(r"\d+", s)
    if len(nums) == 1:
        addr = "R" + nums[0] + "C" + str(letterToInt("".join(re.findall(r"[^\d\W+]",s))))  
        return addr      
    if len(nums) == 2:
        addr = intToLetter(int(nums[1])) + nums[0] 
        return addr       


print(spreadsheet("R65535C65535"))    
print(spreadsheet("CRXO65535"))    