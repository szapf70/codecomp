# https://www.codewars.com/kata/5276c0f3f4bfbd5aae0001ad/train/python
# Grab CSV Columns

def csv_columns(csv, indices):
    res_table = []
    for l in csv.splitlines():
        al = l.split(',')
        ind = [i for i in set(sorted(indices)) if i < len(al)]
        if not ind:
            return ""
        ar = []
        for c in ind:
            if c < len(al):
                ar.append(al[c])
        res_table.append(ar)    
    return "\n".join([",".join(l) for l in res_table])    




print(csv_columns("8,1,5,1,7,1,7,3\n0,2,1,6,4,2,6,8\n5,2,8,1,1,3,2,3\n7,9,3,2,1,9,9,5\n3,3,4,2,7,2,0,2" , [8, 12]))