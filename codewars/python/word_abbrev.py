def doabb(w):
    l = len(w)
    if w.endswith(('!','?','.')) : l -= 1
    if l < 4 : return w
    return w[0] + str(len(w)-2) + w[-1]


def abbreviate(s):
    abb = []
    for w in s.split():
        if w.count('-'):
            abb.append(doabb(w.split('-')[0]) + '-' + doabb(w.split('-')[1]))
        else:
            abb.append(doabb(w))    
    return " ".join(abb)    

print(abbreviate("elephant-rides are really fun!"))
print("e6t-r3s are r4y fun!")