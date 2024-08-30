



n = 4

t1 = 0
t2 = 0
t3 = 0

for x in range(2**n):
    l1 = (x ^ (x // 2))
    l2 = (x ^ (x >> 1))
    l3 = int(x*1.5)
    print(x,l1,l2,l3)
    t1 += l1
    t2 += l2
    t3 += l3
    
    
print(t1,t2,t3)    




