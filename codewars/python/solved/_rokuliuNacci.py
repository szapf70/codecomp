# https://www.codewars.com/kata/5683838837b2d1db32000021/train/python
# Something similar to RokuLiuYeoseot- Nacci

rn = [1,1,2,2,3,3]


def rokuFill(n):
    while len(rn) <= n:
        rn.append(rn[-1]*rn[-2]*rn[-3]-rn[-4]*rn[-5]*rn[-6])
    return rn[n]



def something_acci(num_digits):
    pass

for i in range(6,15):
    erg = rokuFill(i)
    print(i,len(str(erg)))