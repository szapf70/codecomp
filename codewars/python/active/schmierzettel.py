

def logical_calc(arr, op):
    op = " " + op.lower() + " "
    e = op.join([str(f) for f in arr])
    return eval(e)





print(logical_calc([True, False], "AND"), False)
#print(logical_calc([True, False], "OR"), True)
#print(logical_calc([True, False], "XOR"), True)
