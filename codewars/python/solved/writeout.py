# https://www.codewars.com/kata/52724507b149fa120600031d/train/python
# Write out numbers

# https://www.codewars.com/kata/56f4ff45af5b1f8cd100067d/train/python
# Sort - one, three, two



tw = ["zero","one","two","three", "four", "five", "six", "seven","eight","nine",
      "ten","eleven","twelve","thirteen","fourteen", "fifteen", "sixteen", "seventeen",
      "eighteen", "nineteen"]

te = [None,None,"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def number2words(n):
    if n == 0:
        return "zero"

    res = ""
    if n >= 1000:
        res = number2words(n//1000)
        res += " thousand "
        n %= 1000
        if n == 0:
            return res[:-1]

    if n >= 100:
        res += tw[n//100]
        res += " hundred "
        n %= 100
        if n == 0:
            return res[:-1]

    if n <= 19:
        res += tw[n]
    else:
        res += te[n//10]
        n %= 10
        if n == 0:
            return res
        res += "-"+tw[n]
    return res        

def number2words_old(n):
    ln = str(n)
    res = ""
    if n >= 1000:
        res = number2words(int(ln[:-3])) + " thousand "
        ln = ln[-3:]

    if int(ln) >= 100:
        res += tw[int(ln[0])] + " hundred "
        ln = ln[1:]
    print(ln)    
    if 0 < int(ln) <=19:
        res += tw[int(ln[0])]
    else:
        res += te[int(ln[0])]
        if int(ln[1]) > 0:
            res += "-" + tw[int(ln[1])]
            
    return res                

print(number2words(22121))