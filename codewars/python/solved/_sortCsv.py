# https://www.codewars.com/kata/57f7f71a7b992e699400013f/train/python
# Sort the columns of a csv-file

def sort_csv_columns(csv):
    lines = csv.split('\n')
    buf = []
    for e in lines[0].split(';'):
        buf.append((e,[]))
    for l in lines[1:]:
        for i,e in enumerate(l.split(';')):
            print(i,e)
            buf[i][1].append(e)
    buf = sorted(buf, key = lambda e: e[0].lower())  
    res = []
    hdr = []
    for h in buf:
        hdr.append(h[0])
    res.append(";".join(hdr))    
    while len(buf[0][1]) > 0:
        lres = []
        for e in buf:
            lres.append(e[1].pop(0))
        res.append(";".join(lres)) 
    return "\n".join(res)



pre_sorting=(
                    "myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n"
                    "17945;10091;10088;3907;10132\n"
                    "2;12;13;48;11"
                )
post_sorting=(
                    "Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n"
                    "3907;17945;10091;10088;10132\n"
                    "48;2;12;13;11"
                )

print(sort_csv_columns(pre_sorting))