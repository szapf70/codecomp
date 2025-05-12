# https://www.codewars.com/kata/5e1b37bcc5772a0028c50c5d/train/python
# Minimum number of taxis

def min_num_taxis_old(requests):
    t = [[0,0] for _ in range(20000)]
    for pu,do in requests:
        t[pu][0] += 1
        t[do][1] += 1
    taxis = 0
    max_taxis = 0
    for pu,do in t:
        taxis += pu
        if taxis > max_taxis: max_taxis = taxis
        taxis -= do
    return max_taxis

def min_num_taxis(requests):
    requests = sorted(requests)
    t = {}
    max_taxis = 0
    taxis = 0 
    for pu,do in requests:
        print(pu,do,taxis, max_taxis,t)
        
        for k in range(do):
            if k in t:
                taxis -= t[k]
                t.pop(k)
        
        t[do] = t.get(do, 0) + 1
        taxis += 1
        if taxis > max_taxis: max_taxis = taxis
    return max_taxis    


t = [(27, 28), (2, 27), (13, 18), (4, 16), (1, 28), (11, 17), (3, 27), (2, 22), (29, 30), (20, 29), (22, 24), (21, 23), (18, 30), (7, 18), (3, 13)]
four_reqs = [(1,4), (2, 9), (3, 6), (5, 8)]
print(min_num_taxis_old(t))