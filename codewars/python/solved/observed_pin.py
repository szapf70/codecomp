# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
# The observed PIN
  
def expadj(li, next):
    ladj = { '0' : "08",
             '1' : "124",
             '2' : "2135",
             '3' : "326",
             '4' : "4157",
             '5' : "24568",
             '6' : "3569",
             '7' : "478",
             '8' : "57890",
             '9' : "689"
            }
    lres = []
    if li == []:
        for l in ladj[next]:
            lres.append(l)
        return lres    
    for elem in li:
        for l in ladj[next]:
            lres.append(elem + l)
    return lres    

def get_pins(observed):
    prog= []
    for n in observed:
        prog = expadj(prog, n)

    return prog





print(get_pins('369'))