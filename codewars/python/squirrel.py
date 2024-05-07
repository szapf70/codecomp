def zero(n="0"): 
    if len(n) == 1: return n
    else: return calc("0"+n)
def one(n="1"): 
    if len(n) == 1: return n
    else: return calc("1"+n)
def two(n="2"): 
    if len(n) == 1: return n
    else: return calc("2"+n)
def three(n="3"): 
    if len(n) == 1: return n
    else: return calc("3"+n)
def four(n="4"): 
    if len(n) == 1: return n
    else: return calc("4"+n)
def five(n="5"): 
    if len(n) == 1: return n
    else: return calc("5"+n)
def six(n="6"): 
    if len(n) == 1: return n
    else: return calc("6"+n)
def seven(n="7"): 
    if len(n) == 1: return n
    else: return calc("7"+n)
def eight(n="8"): 
    if len(n) == 1: return n
    else: return calc("8"+n)
def nine(n="9"): 
    if len(n) == 1: return n
    else: return calc("9"+n)


def plus(o): return "+"+o
def minus(o): return  "-"+o
def times(o): return  "*"+o
def divided_by(o): return  "/"+o

def calc(mstr): 
    o1 = int(mstr[0])
    o2 = int(mstr[2])
    op = mstr[1]
    match op:#
        case '+' : return o1+o2
        case '-' : return o1-o2
        case '*' : return o1*o2
        case '/' : return int(o1/o2)

print(seven(times(five())))


"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))

"""