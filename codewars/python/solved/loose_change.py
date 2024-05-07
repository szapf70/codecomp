# https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/python
# Loose Change

def loose_change(cents):
    loose = {'Nickels' : 0, 'Pennies' : 0, 'Dimes' : 0, 'Quarters' : 0}
    lc = int(cents)
    if lc <= 0: 
        return loose
    
    for cur,val in [( 'Quarters' , 25),( 'Dimes' , 10),('Nickels',5),('Pennies' , 1)]:
        while lc >= val:
            lc -= val
            loose[cur] += 1
            if lc == 0:
                return loose


print(loose_change(3.9))