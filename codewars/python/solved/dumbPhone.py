# https://www.codewars.com/kata/5680e56f4797a55076000044/train/python
# Dumbphone Keypads

def sequence(phrase):
    li = {"A" : "2", "B" : "22", "C" : "222", "2" : "2222",
          "D" : "3", "E" : "33", "F" : "333", "3" : "3333",
          "G" : "4", "H" : "44", "I" : "444", "4" : "4444",
          "J" : "5", "K" : "55", "L" : "555", "5" : "5555",
          "M" : "6", "N" : "66", "O" : "666", "6" : "6666",
          "P" : "7", "Q" : "77", "R" : "777", "S" : "7777", "7" : "77777",
          "T" : "8", "U" : "88", "V" : "888", "8" : "8888",
          "W" : "9", "X" : "99", "Y" : "999", "Z" : "9999", "9" : "99999",
          "*" : "*", 
          " " : "0",
          "#" : "#"}
    last = None
    res = ""
    for l in phrase:
        temp = li[l.upper()]
        if temp[0] == last: res += "p"
        last = temp[0]
        res += temp
    return res    

print(sequence("HELLO WORLD"))
print("4433555p555666096667775553")
"""
------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |space| |     |
|  *  | |  0  | |  #  |
------- ------- -------
"""