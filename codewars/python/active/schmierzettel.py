from itertools import groupby

a = [1,1,1,2,2,2,3,3,3,1,1,1,2,2,3,3,3]
for e,f in groupby(a):
    print(e,list(f))


