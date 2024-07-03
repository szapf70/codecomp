# https://www.codewars.com/kata/583710f6b468c07ba1000017/train/python
# Proof Read

def proofread(st):
    res = []
    for s in st.replace('. ', '.').split('.'):
        if s != "":
            s = s.lower().replace('ie', 'ei').strip()
            res.append(s[0].upper() + s[1:] + '.')

    return " ".join(res)               




print(proofread("THe neIghBour's ceiLing FEll on His Head. The WiEght of It crusHed him To thE gROuNd."))
print("The neighbour's ceiling fell on his head. The weight of it crushed him to the ground.")