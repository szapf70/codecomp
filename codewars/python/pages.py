# https://www.codewars.com/kata/622de76d28bf330057cd6af8/train/python
# How many pages in a book?

def amount_of_pages(summary):
    pb = [{'start' : 1, 'end' : 9, 'len' : 1,'max' : 9},
          {'start' : 10,'end' : 99,'len' : 2,'max' : 178},
          {'start' : 100,'end' : 999,'len' : 3,'max' : 2_697},
          {'start' : 1_000,'end' : 9_999,'len' : 4,'max' : 35_996},
          {'start' : 10_000,'end' : 99_999,'len' : 5,'max' : 449_995},
          {'start' : 100_000,'end' : 999_999,'len' : 6,'max' : 5_399_994 }]

    ls = summary
    ap = 0
    pbi = 0

    while pb[pbi]['max'] < ls:
        ls -= pb[pbi]['max']
        ap += pb[pbi]['max']//pb[pbi]['len']
        pbi += 1
    

    ap += round(ls//pb[pbi]['len']+0.5,0)



    return ap    

print(amount_of_pages(5), 5)
print(amount_of_pages(25), 17)
print(amount_of_pages(1095), 401)        
print(amount_of_pages(185), 97)
print(amount_of_pages(660), 256)
