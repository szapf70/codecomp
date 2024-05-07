# https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python
# What century is it?



def what_century_old(year):
    ending = ["th","st","nd","rd","th","th","th","th","th","th","th",]
    ly = int(year)
    y = (ly//100)
    if ly%1000 > 0: y+=1
    estr = ""
    if y < 5: estr = ending[y]
    else: estr = "th"
    return str(y) + estr  
    
def what_century(year):
    ending = ["th","st","nd","rd","th","th","th","th","th","th","th","th","th","th"]
    ly = int(year)
    y = (ly//100)
    if ly%100 > 0: y+=1
    estr = ""
    if y < 14: 
        estr = ending[y%100]
    else:
        estr = ending[y%10]    
    return str(y) + estr 
    
  



    pass            
    #
    # return []



print(what_century("2259"))
print(what_century("2000"))
print(what_century("223"))
