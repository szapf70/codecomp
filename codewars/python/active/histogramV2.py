# https://www.codewars.com/kata/5d5f5f25f8bdd3001d6ff70a/train/python
# Histogram - V2

def histogram(rolls):
    ext6 = False
    if rolls[5] > 9:
        ext6 = True
    rc = [n if n > 0 else -1 for n in rolls]
    rows = []   
    if max(rolls) > 0:
        for _ in range(max(rolls)+1):
            lrow = ""
            for y in range(6):
                if rc[y] > 0:
                    lrow += '# '
                if rc[y] == 0:
                    lrow += str(rolls[y]).ljust(2)
                if rc[y] < 0:
                    lrow += '  '        
            rc = [n-1 for n in rc]
            rows.append(lrow)
        rows = [r.rstrip() for r in rows[::-1]]
    else:    
        rows.append('')

    l = '-----------'
    rows.append(l)
    rows.append('1 2 3 4 5 6\n')
    return "\n".join(rows)



roll = [7,3,10,1,0,5]
roll2 = [11,9,6,9,5,10]
print(histogram(roll2))

