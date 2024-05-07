# https://www.codewars.com/kata/56f3ed90de254a2ca7000e20/train/python
# Find the discounted prices



def find_discounted(prices):
    pl = list(map(int,prices.split()))
    dp = []
    while len(pl) > 0:
        pd = pl.pop(0)
        fi = pl.index(int((pd//3)*4))
        
        if  fi != -1:
            dp.append(pd)
            pl.pop(fi)
    return " ".join([str(n) for n in dp])        
            
print(find_discounted("9 9 12 12 12 15 16 20"))        