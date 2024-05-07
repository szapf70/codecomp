# https://www.codewars.com/kata/52724507b149fa120600031d/train/python
# Write out numbers

# https://www.codewars.com/kata/56f4ff45af5b1f8cd100067d/train/python
# Sort - one, three, two

# https://www.codewars.com/kata/53c94a82689f84c2dd00007d/train/python
# Integer to English



import sys

blocks = ['thousand','million','billion',
          'trillion','quadrillion','quintillion', 
          'sextiilion','septillion', 'octillion',
          'nonillion', 'decillion', 'undecillion',
          'duodecillion','tredecillion']



tw = ["zero","one","two","three", "four", "five", "six", "seven","eight","nine",
      "ten","eleven","twelve","thirteen","fourteen", "fifteen", "sixteen", "seventeen",
      "eighteen", "nineteen"]

te = [None,None,"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def hblock(b):
    rstr = ""
    if b >= 100:
        rstr = tw[b//100] + " hundred "
        b %=100
    if 0 < b <=19:
        rstr += tw[b]
    else:
        rstr += te[b//10]
        if b%10 != 0:
            rstr += " " + tw[b%10]
    if b == 0:
        return ''        
    return rstr

def int_to_english(n):
    parts = []
    while True:
        if n < 1000:
            parts.append(hblock(n))
            break
        if n >= 1000:
            parts.append(hblock(n%1000))
            n = n // 1000

    rparts = [parts.pop(0)]
    
    while len(parts) > 0:
        rparts.insert(0,blocks.pop(0))
        rparts.insert(0,parts.pop(0))

    return " ".join(rparts)





print(int_to_english(2000))
