t = {"abc" : 1,
     "cde" : 3,
     "bbb" : 4,
     "eee" : 2}

print(sorted(list(zip(t.values(),t.keys()))))