# https://www.codewars.com/kata/52fea6fd158f0576b8000089/train/python
# ASCII hex converter

class Converter():
    @staticmethod
    def to_ascii(h):
        res = ""
        while h:
            lh = h[:2]
            res += chr(int(lh,16))
            h = h[2:]
        return res    
    
    @staticmethod
    def to_hex(s):
        res = ""
        for l in s:
            res += hex(ord(l))[2:]
        return res    
    
    
s = "Look mom, no hands"
h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"

print(hex(122))
print(int("7a",16))
