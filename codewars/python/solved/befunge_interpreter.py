# https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python
# Befunge Interpreter

from random import choice

def interpret(source):
    code = []
    for line in source.split('\n'):
        code.append(list(line))        
    
    st = [] # Stack
    dir = 'right'
    x = 0
    y = 0
    output = ""
    strmode = False
    
    def _pop():
        if st == []:
            return 0
        return st.pop()
    
    def _push(e):
        st.append(e)
    
    def _step(y,x):
        match dir:
            case 'up':
                if y > 0: y = y -1
                else:     y = len(code)-1
            case 'down':
                if y < len(code)-1: y = y + 1
                else:               y = 0 
            case 'right':
                if x < len(code[y])-1: x = x + 1
                else:                x = 0
            case 'left':
                if x > 0: x = x - 1
                else: x = len(code[y])-1
        return y,x
    # Endlos
    while True:
        inst = code[y][x]
        print(f"INST:{inst} - Y:{y}/X:{x} - DIR:{dir} - STACK:{st} - OUTPUT:{output}")
        if strmode:
            if inst == '"':
                strmode = False
            else:    
                _push(ord(inst))
            y, x = _step(y,x)
            continue 
        match inst:
        # > Start moving right.
        # < Start moving left.
        # ^ Start moving up.
        # v Start moving down.
        # ? Start moving in a random cardinal direction.
            case '>':
                dir = 'right'
            case '<':
                dir = 'left'
            case '^':
                dir = 'up'
            case 'v':
                dir = 'down'      
            case '?':
                dir = choice(['right','left','up','down'])
        # _ Pop a value; move right if value = 0, left otherwise.
        # | Pop a value; move down if value = 0, up otherwise.
            case '_':
                dir = 'left' if _pop() else 'right'
            case '|':
                dir = 'up' if _pop() else 'down'  
        # # Trampoline: Skip next cell.
            case '#':
                y, x = _step(y,x)
        # 0-9 Push this number onto the stack.    
            case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                _push(int(inst))
        # + Addition: Pop a and b, then push a+b.
        # - Subtraction: Pop a and b, then push b-a.
        # * Multiplication: Pop a and b, then push a*b.
        # / Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
        # % Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
            case '+':
                _push(_pop()+_pop())
            case '-':
                a = _pop()
                b = _pop()
                _push(b-a)  
            case '*':
                _push(_pop()*_pop())
            case '/':
                a = _pop()
                b = _pop()
                _push(b//a)
            case '%':
                a = _pop()
                b = _pop()    
                if not a:
                    _push(0)
                else:
                    _push(b%a)
        # ! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
        # ` (backtick) Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.
            case '!':
                l = _pop()
                _push(0 if l else 1)
            case '`':
                a = _pop()
                b = _pop()
                _push(1 if b > a else 0)      
        # : Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.
        # \ Swap two values on top of the stack. If there is only one value, pretend there is an extra 0 on bottom of the stack.
        # $ Pop value from the stack and discard it.
            case ':':
                v = _pop()
                _push(v)
                _push(v)
            case '\\':
                a = _pop()
                b = _pop()
                _push(a)
                _push(b)
            case '$':
                _pop()
        # . Pop value and output as an integer.
        # , Pop value and output the ASCII character represented by the integer code that is stored in the value.
            case '.':
                output += str(_pop())
            case ',':
                output += chr(_pop())          
        # p A "put" call (a way to store a value for later use). Pop y, x and v, then change the character at 
        #   the position (x,y) in the program to the character with ASCII value v.
        # g A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the character 
        #   at that position in the program.
        # (i.e. a space) No-op. Does nothing.
            case 'p':  
                _y = _pop()
                _x = _pop()
                _v = _pop()
                code[_y][_x] = chr(_v)
            case 'g':
                _y = _pop()
                _x = _pop()
                _push(ord(code[_y][_x]))
            case ' ':
                pass  
        # " Start string mode: push each character's ASCII value all the way up to the next ".
            case '"':
                strmode = True
        # @ End program.
            case '@':
                return output  
            case _:
                raise Exception(f'Unknown instruction {inst} at {y}|{x}')
        # Last instr of the while
        y, x = _step(y,x)
 
    #return code



f1 = '>987v>.v\nv456<  :\n>321 ^ _@'
print(interpret(f1))

"""
Esoteric languages are pretty hard to program, but it's fairly interesting to write interpreters for them!

Your task is to write a method which will interpret Befunge-93 code! Befunge-93 is a language in which the code is presented not as a 
series of instructions, but as instructions scattered on a 2D plane; your pointer starts at the top-left corner and defaults to moving right 
through the code. Note that the instruction pointer wraps around the screen! There is a singular stack which we will assume is unbounded and 
only contain integers. While Befunge-93 code is supposed to be restricted to 80x25, you need not be concerned with code size. Befunge-93 
supports the following instructions (from Wikipedia):

f0-9 Push this number onto the stack.
f+ Addition: Pop a and b, then push a+b.
f- Subtraction: Pop a and b, then push b-a.
f* Multiplication: Pop a and b, then push a*b.
f/ Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
f% Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
f! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
f` (backtick) Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.
f> Start moving right.
f< Start moving left.
f^ Start moving up.
fv Start moving down.
f? Start moving in a random cardinal direction.
f_ Pop a value; move right if value = 0, left otherwise.
f| Pop a value; move down if value = 0, up otherwise.
" Start string mode: push each character's ASCII value all the way up to the next ".
f: Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.
f\ Swap two values on top of the stack. If there is only one value, pretend there is an extra 0 on bottom of the stack.
f$ Pop value from the stack and discard it.
f. Pop value and output as an integer.
f, Pop value and output the ASCII character represented by the integer code that is stored in the value.
f# Trampoline: Skip next cell.
fp A "put" call (a way to store a value for later use). Pop y, x and v, then change the character at the position (x,y) in the program to the 
character with ASCII value v.
fg A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the character at that position in the program.
f@ End program.
f  (i.e. a space) No-op. Does nothing.
The above list is slightly modified: you'll notice if you look at the Wikipedia page that we do not use the user input instructions and 
dividing by zero simply yields zero.

Here's an example:

>987v>.v
v456<  :
>321 ^ _@
will create the output 123456789.

So what you must do is create a function such that when you pass in the Befunge code, the function returns the output that would be generated 
by the code. So, for example:

"123456789".equals(new BefungeInterpreter().interpret(">987v>.v\nv456<  :\n>321 ^ _@")
This test case will be added for you.

>987v>.v
v456<  :
>321 ^ _@
"""