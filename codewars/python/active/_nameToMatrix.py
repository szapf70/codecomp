# https://www.codewars.com/kata/5a91e0793e9156ccb0003f6e/train/python
# Name to Matrix


def matrixfy(st):
    qlen = len(st)**0.5
    if qlen > int(qlen):
        qlen += 1
    qlen = int(qlen)    
    st = st.ljust(qlen**2,'.')
    res = [] 
    for i in range(0,qlen**2,qlen):
        res.append(list(st[i:i+qlen]))   
    return res

print(matrixfy("123456"))

#print(math.log(7,2))
