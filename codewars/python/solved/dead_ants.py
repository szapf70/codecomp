# https://www.codewars.com/kata/57d5e850bfcdc545870000b7/train/python
# Dead Ants




# string ants
def dead_ant_count (ants):
    a = ants.replace('ant', '*')
    return max(a.count('a'),a.count('n'),a.count('t'))
    
    
    

print(dead_ant_count("antantantan"))