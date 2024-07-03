# https://www.codewars.com/kata/58a664bb586e986c940001d5/train/python
# Simple Fun #135: Missing Alphabets

def missing_alphabets(st):
    ba = list("abcdefghijklmnopqrstuvwxyz")
    res = ba.copy()
    for l in st:
        if l in res:
            res.remove(l)
        else:
            res.extend(ba)
            res.remove(l)
    return "".join(sorted(res))  


print(missing_alphabets("abcdefghijklmnopqrstuvwxy"),"z")
#print(missing_alphabets("abcdefghijklmnopqrstuvwxyz"),"")
#print(missing_alphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy"),"zz")
#print(missing_alphabets("abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy"),"ayzz")
#print(missing_alphabets("codewars"),"bfghijklmnpqtuvxyz")