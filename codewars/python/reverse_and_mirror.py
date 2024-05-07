def reverse_and_mirror(s1, s2):
    s1s = "".join([l.lower() if l==l.upper() else l.upper() for l in list(s1)])
    s2s = "".join([l.lower() if l==l.upper() else l.upper() for l in list(s2[::-1])])
    return s2s + "@@@" + s1s[::-1] + s1s

print(reverse_and_mirror("FizZ","buZZ"))


