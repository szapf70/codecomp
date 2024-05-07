# https://www.codewars.com/kata/58925dcb71f43f30cd00005f/train/python
# The latest clock

def check_nums(narray,tparts):
    for t in tparts:
        if narray.count(t) < tparts.count(t):
            return False
    return True    
    
    


def latest_clock(a, b, c, d):
    n = [str(a),str(b),str(c),str(d)]
    for i in range(23,-1,-1):
        lhours =""
        lminutes = ""
        ln = n.copy()
        lnstr = str(i).rjust(2,"0")
        if check_nums(ln,[lnstr[0],lnstr[1]]):
            lhours = lnstr
            ln.remove(lnstr[0])
            ln.remove(lnstr[1])
            for j in range(59,-1,-1):
                lnstr = str(j).rjust(2,"0")
                if check_nums(ln,[lnstr[0],lnstr[1]]):
                    lminutes = lnstr
                    return lhours + ":" + lminutes                                




print(latest_clock(9, 2, 1, 9))

"""

"""