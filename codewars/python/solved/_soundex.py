# https://www.codewars.com/kata/587319230e9cf305bb000098/train/python
# Soundex

def soundex(name):
    p = name.lower().split()
    res = []
    for n in p:
        first = n[0]
        n = first + n[1:].replace('h', '').replace('w', '')
        n = n.translate(str.maketrans('bfpvcgjkqsxzdtlmnr', '111122222222334556'))            

        ln = ""

        if len(n) > 0:
            for r in n:
                if ln == "":
                    ln += r
                else:
                    if ln[-1] != r:
                        ln += r


        for r in "aeiouy":
            ln = ln[0] + ln[1:].replace(r, '')

        if ln[0].isdigit():
            ln = first + ln[1:]

        ln = ln[0].upper() + ln[1:]

        ln+= '000'
        res.append(ln[:4]) 

    return " ".join(res)    


#print(soundex("Sarah Connor"))
print(soundex("Tymczak"))
print(soundex("Pfister"))

"""
In this Kata you will encode strings using a Soundex variation called "American Soundex" using the following (case insensitive) steps:

Save the first letter. Remove all occurrences of h and w except first letter.
Replace all consonants (include the first letter) with digits as follows:
b, f, p, v = 1
c, g, j, k, q, s, x, z = 2
d, t = 3
l = 4
m, n = 5
r = 6
Replace all adjacent same digits with one digit.
Remove all occurrences of a, e, i, o, u, y except first letter.
If first symbol is a digit replace it with letter saved on step 1.
Append 3 zeros if result contains less than 3 digits. Remove all except first letter and 3 digits after it
Input
A space separated string of one or more names. E.g.

Sarah Connor

Output
Space separated string of equivalent Soundex codes (the first character of each code must be uppercase). E.g.

S600 C560


"""
