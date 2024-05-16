# https://www.codewars.com/kata/56f2dd31e40b7042ad001026/train/python
# Endianness Conversion

# Switch the endianness of integer n
def switch_endian(n, bits):
    nstr = bin(n)[2:]
    if len(nstr) > bits:
        return nstr
    nstr = nstr.zfill(bits)
    return nstr
    





print(switch_endian(200,16))
