# https://www.codewars.com/kata/5827e2efc983ca6f230000e0/train/python
# Complete the table pattern

def roof(cols):
    return "---".join(['+'] * (cols + 1))

def pattern(rows, columns, s):
    def roof(cols):
        return "---".join(['+'] * (cols + 1))
    s = list(map(lambda c: " "+c+" ", s.ljust(rows*columns)))
    r = []
    while s:
        r.append(s[:columns])
        s = s[columns:]
    
    res = []
    res.append(roof(columns))
    for e in r:
        res.append("|" + "|".join(e) + "|")
        res.append(roof(columns))
        
    return "\n".join(res)



#print(roof(4))
print(pattern(4, 4, "Hello World!"))