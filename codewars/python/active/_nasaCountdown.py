# https://www.codewars.com/kata/56c4931400165c5283000661/train/python
# NASA Countdown

def countdown(milliseconds):
    v = "+" if milliseconds >= 0 else ""
    c = milliseconds//1000
    s = c%60
    c //=60
    m = c%60
    c//=60
    h = c
    return v + ":".join([str(h).rjust(2,"0"),str(m).rjust(2,"0"),str(s).rjust(2,"0")])


print(countdown(-154800000))