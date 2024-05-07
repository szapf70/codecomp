# https://www.codewars.com/kata/585cf93f6ad5e0d9bf000010/train/python
# Bowling Pins

def bowling_pins(arr : list[int]) -> str:
    def p(n):
        return " " if n in arr else "I"

    return f"{p(7)} {p(8)} {p(9)} {p(10)}\n {p(4)} {p(5)} {p(6)} \n  {p(2)} {p(3)}  \n   {p(1)}   "



print(bowling_pins([1,2,10]))

"""
for [1, 2, 10]
: 
'I I I  \n
  I I I \n
   I  \n
    I   ' 
    
'I I I  \n
I I I \n
I  \n       '






"""