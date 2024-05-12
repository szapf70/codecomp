



arr = [345, 32, 45, 12, 45, 47, 49, 55, 90, 104, 20, 30, 34]
#arr = [10,9,8,7,6,5,4,3,2,1]

top = {"l" : 0, "s" : 0, "e" : 0}
act = {"l" : 0, "s" : 0, "e" : 0}
run = False

i = 2
while i < len(arr):
    if arr[i-2] < arr[i-1] < arr[i]:
        if run:
            act['l'] += 1
        else:
            act['l'] = 3
            act['s'] = i -2
            run = True
    else:
        if run:
            act['e'] = i - 1
            run = False
            if act['l'] > top['l']:
                top = act  
                act = {'l' : 0, 's' : 0,'e' :0}     

    i += 1

print(top,arr[top['s']:top['e']+1])    