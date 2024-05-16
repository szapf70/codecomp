# https://www.codewars.com/kata/55e4419eb589793709000044/train/python
# Closest Neighbouring Points I

def closest_points(lst_points):
    sd = 2**31-1
    buf = []
    res = []
    for i in range(0,len(lst_points)-1):
        for j in range(i+1,len(lst_points)):
            d = ((lst_points[i][0]-lst_points[j][0])**2 + (lst_points[i][1]-lst_points[j][1])**2)**0.5
            if d < sd: sd = d
            buf.append([lst_points[i], lst_points[j], d])
    for b in buf:
        if b[2] == sd:
            res.append(sorted([b[0],b[1]]))
    res = sorted(res)
    return [len(lst_points),res,round(sd,4)]        

def closest_points_3d(lst_points):
# PQ = d = √ [(x2 – x1)2 + (y2 – y1)2 + (z2 – z1)2].
    sd = 2**31-1
    buf = []
    res = []
    for i in range(0,len(lst_points)-1):
        for j in range(i+1,len(lst_points)):
            d = ((lst_points[i][0]-lst_points[j][0])**2 + (lst_points[i][1]-lst_points[j][1])**2 + (lst_points[i][2]-lst_points[j][2])**2)**0.5
            if d < sd: sd = d
            buf.append([lst_points[i], lst_points[j], d])
    for b in buf:
        if b[2] == sd:
            res.append(sorted([b[0],b[1]]))
    res = sorted(res)
    return [len(lst_points),res,round(sd,5)]        





print(closest_points_3d([(9, 8, 5), (4, 2, 3), (10, 7, 4), (0, 9, 7), (3, 2, 6), (5, 8, 4),\
         (1, 9, 6), (4, 5, 6), (5, 10, 10), (8, 8, 2)]))
print([10, [[(0, 9, 7), (1, 9, 6)]], 1.41421])



"""
listPointsII = [(8, 14), (16, 5), (5, 5), (15, 18), (17, 10), (0, 14), (4, 15),\
         (19, 17), (13, 16), (10, 18), (14, 13), (12, 14), (11, 15), (7, 15)]
print(closest_points(listPointsII))
print([14, [[(7, 15), (8, 14)], [(11, 15), (12, 14)]], 1.4142])
"""