# https://www.codewars.com/kata/57c15d314677bb2bd4000017/train/python
# Doors in the school

def doors(n):
    d = [False] * (n+1)
    inter = 1

    for _ in range(n):
        for i in range(inter,n,inter):
            d[i] = not d[i]

    return d



print(doors(5))        