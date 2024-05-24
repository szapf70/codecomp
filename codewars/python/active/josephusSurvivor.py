# https://www.codewars.com/kata/555624b601231dc7a400017a/train/python
# Josephus Survivor

# https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python
# Josephus Permutation

def josephus_survivor(n,k):
    print(n,k)
    list = [i for i in range(1,n+1)]
    idx = 0
    while len(list) > 1:
        idx = idx + k-1
        idx = idx%len(list)
        list.pop(idx)
    return list[0]    


def josephus(items,k):
    idx = 0
    perm = []
    while len(items) > 1:
        idx = idx + k-1
        idx = idx%len(items)
        perm.append(items.pop(idx))
    perm.append(items[0])
    return perm    


    #your code here
    return []




print(josephus([1,2,3,4,5,6,7],3))




"""
n=7, k=3 => means 7 people in a circle
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!

"""