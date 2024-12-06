import re

def find_mul_patterns(text):
    # Muster für die Suche nach 'mul(' gefolgt von zwei Zahlen, die durch ein Komma getrennt sind und ')' am Ende
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, text)
    return matches

res = 0

def mul(a,b):
    res += a*b


memory = None

with open('day_03.txt') as f:
    memory = f.read()    


result = find_mul_patterns(memory)



for b in result:
    x,y = b[4:-1].split(',')
    res += int(x)*int(y)
    
print(res)    
