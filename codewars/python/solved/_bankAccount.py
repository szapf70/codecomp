# https://www.codewars.com/kata/597eeb0136f4ae84f9000001/train/python
# Parse bank account number

def parse_bank_account(ba):
    ds = {" _ | ||_|" : "0",
          "     |  |" : "1",
          " _  _||_ " : "2",
          " _  _| _|" : "3",
          "   |_|  |" : "4",
          " _ |_  _|" : "5",
          " _ |_ |_|" : "6",
          " _   |  |" : "7",
          " _ |_||_|" : "8",
          " _ |_| _|" : "9"}
    
    bas = ba.rstrip("\n").split("\n")
    
    bl = len(bas[0])//3
    bzf = [""] * bl

    for l in bas:
        ni = 0
        while len(l) > 0:
            bzf[ni] += l[:3]
            l = l[3:]
            ni += 1
    
    res = ""    
    
    for n in bzf:
        res += ds[n]

    return int(res)
       

text = '    _  _     _  _  _  _  _ \n'+ '  | _| _||_||_ |_   ||_||_|\n'+   '  ||_  _|  | _||_|  ||_| _|\n'

print(parse_bank_account(text))