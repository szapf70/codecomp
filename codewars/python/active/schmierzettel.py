def group_in_10s(*args):
    res = [None] * ((max(args))//10+1)
    for n in args:
        i = n//10
        if res[i] == None:
            res[i] = []
        res[i].append(n)
    return [sorted(a) if a else None for a in res]

print(group_in_10s(8, 12, 38, 3, 17, 19, 25, 35, 50))
          
