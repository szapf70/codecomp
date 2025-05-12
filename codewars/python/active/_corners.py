# https://www.codewars.com/kata/58ed139326f519019a000053/train/python
# Northwest and Southeast corners

def box(coords):
    fl = []
    sl = []
    for f,s in coords:
        fl.append(f) 
        sl.append(s)
    return {"nw" : [max(fl),min(sl)], "se" : [min(fl),max(sl)]}    

print(box([ [ -32, -143 ], [ 68, 165 ], [ -32, -130 ],
        [ -14, 118 ], [ -48, -136 ], [ 15, 29 ], [ -70, 50 ], [ -14, -179 ], 
        [ 35, -72 ], [ 8, -19] ]))


#, { "nw": [ 68, -179 ], "se": [ -70, 165 ] })