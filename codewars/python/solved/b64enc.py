# https://www.codewars.com/kata/5632e12703e2037fa7000061/train/python
# Base64 Numeric Translator


def to_base_64(string):
    pass
#your code here
    
def from_base_64(string):
    pass
#your code here
    
    
def makebin():
    return bin(123456789091827645463787687687688)   

def b64tobin(b64str):
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    res = 0
    for p,d in enumerate(b64str[::-1]):
        res += digits.index(d)*(64**p)
    return bin(res)[2:]    
    
def bin2base256(binstr):
    res = ""
    while len(binstr) >=8:
        print(binstr)
        print(binstr[:8])
        print(int(binstr[:8],2))
        res += chr(int(binstr[:8],2))
        binstr = binstr[8:]
    return res            
    
def base64_to_base10(s):
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    res = 0
    for p,d in enumerate(s[::-1]):
        res += digits.index(d)*(64**p)
    return res       

temp = b64tobin("MTIzNDU2Nzg5MCAg")
print(bin2base256(temp))
#print(int("1010",2))
#print(b64tobin("MTIzNDU2Nzg5MCAg"))
#print(str(b64tobin("MTIzNDU2Nzg5MCAg")))
