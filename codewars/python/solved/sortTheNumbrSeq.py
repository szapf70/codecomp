# https://www.codewars.com/kata/5816b76988ca9613cc00024f/train/python
# Sort the number sequence

def sort_sequence(sequence):
    pre = []
    buf = []
    cnt = 0
    for n in sequence:
        print(n)
        if n == 0:
            pre.append((sum(buf),cnt,sorted(buf).copy()))
            cnt += 1
            buf.clear()
        else:
            buf.append(n)
    pre = sorted(pre, key = lambda x: (x[0], x[1]))

    res = []
    for p in pre:
        res.extend(p[2])
        res.append(0)
    return res

print(sort_sequence([2,2,2,0,5,6,4,0,1,5,3,0,3,2,1,0]))




"""
sortSequence([3,2,1,0,5,6,4,0,1,5,3,0,4,2,8,0]) should return
[1,2,3,0,1,3,5,0,2,4,8,0,4,5,6,0]

sortSequence([3,2,1,0,5,6,4,0,1,5,3,0,2,2,2,0]) should return
[1,2,3,0,2,2,2,0,1,3,5,0,4,5,6,0]

sortSequence([2,2,2,0,5,6,4,0,1,5,3,0,3,2,1,0]) should return
[2,2,2,0,1,2,3,0,1,3,5,0,4,5,6,0]
"""