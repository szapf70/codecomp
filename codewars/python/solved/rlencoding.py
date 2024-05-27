# https://www.codewars.com/kata/57d6c3fb950d84fcfb0015c8/train/python
# Compress/Encode a Message with RLE (Run Length Encoding)

def encode(inp):
    res = ""
    last = None
    lc =0
    for l in inp:
        if last == l:
            lc += 1
        if last != l:
            if lc == 0:
                last = l
                lc = 1        
            else:
                res += last
                res += str(lc)
                last = l
                lc = 1
    res += last
    res += str(lc)
    return res

print(encode("HELLO WORLD"))
print("H1E1L2O1 1W1O1R1L1D1")
"""
Run Length Encoding is used to compress data. RLE works like this: characters = "AAAALOTOOOOFTEEEEXXXXXXT" then the encoding will store AAAA = A4 and L1 So all together:

encode("AAAALOTOOOOFTEEEEXXXXXXT") == "A4L1O1T1O4F1T1E4X6T1"
# or
encode("HELLO WORLD") == "H1E1L2O1 1W1O1R1L1D1"
# or
encode("FOO+BAR") == "F1O2+1B1A1R1"
as you can see, its not always as efficient, but with some specific data it works!


"""