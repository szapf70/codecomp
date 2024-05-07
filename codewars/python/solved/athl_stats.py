# https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python
# Statistics for an Athletic Association

import statistics

def stat(strg):
    def st(s):
        h = s // 3600
        s %= 3600
        m = s // 60
        s %= 60
        return f"{str(h).rjust(2,'0')}|{str(m).rjust(2,'0')}|{str(s).rjust(2,'0')}"

    raw_e = strg.split(', ')
    sl = []
    for e in raw_e:
        h,m,s = e.split('|')
        sl.append(int(s) + int(m)*60 + int(h)*3600)
    
    r = max(sl)-min(sl)
    a = int(statistics.mean(sl))
    m = int(statistics.median(sl))   
    return f"Range: {st(r)} Average: {st(a)} Median: {st(m)}"


print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))
     
