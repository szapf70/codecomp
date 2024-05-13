# https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python
# Befunge Interpreter

from random import choice

def interpret(code):
    x = 0
    y = 0
    d = None
    st = []
    output = ""

    def _pop():
        if st:
            return st.pop()
        return 0


    while code[y][x] != '@':
        instr = code[y][x]

        # Numbers to Stack
        if instr in "0123456789":
            st.append(int(instr))

        # Math ops
        if instr in "+-*/%":
            a = st.pop()
            b = st.pop()
            match instr:
                case '+':
                    st.append(a+b)            
                case '-':
                    st.append(b-a) 
                case '*':
                    st.append(a*b)
                case '/':
                    if a == 0:
                        st.append(0)
                    else:
                        st.append(b//a)
                case '%':
                    if a == 0:
                        st.append(0)
                    else:
                        st.append(b%a)
                        
        # NOT "!"                
                                                                               

        # Directions '<>^v?'
        if instr in '<>^v?':
            if instr == '<': d = (-1, 0) 
            if instr == '>': d = (1 ,0)
            if instr == '^': d = (0,-1)
            if instr == 'v': d = (0,1)               
            if instr == '?':
                d = choice([(-1, 0),(1 ,0),(0,-1),(0,1)])
      
        # Skip next cell '#'
        if instr == '#':        
            x += d[0]
            y += d[1]

        # Next instruction
        x += d[0]
        y += d[1]
        # end of while
        
        
    
    
    
    return output

"""
Esoteric languages are pretty hard to program, but it's fairly interesting to write interpreters for them!

Your task is to write a method which will interpret Befunge-93 code! Befunge-93 is a language in which the code is presented not as a 
series of instructions, but as instructions scattered on a 2D plane; your pointer starts at the top-left corner and defaults to moving right 
through the code. Note that the instruction pointer wraps around the screen! There is a singular stack which we will assume is unbounded and 
only contain integers. While Befunge-93 code is supposed to be restricted to 80x25, you need not be concerned with code size. Befunge-93 
supports the following instructions (from Wikipedia):

0-9 Push this number onto the stack.
+ Addition: Pop a and b, then push a+b.
- Subtraction: Pop a and b, then push b-a.
* Multiplication: Pop a and b, then push a*b.
/ Integer division: Pop a and b, then push b/a, rounded down. If a is zero, push zero.
% Modulo: Pop a and b, then push the b%a. If a is zero, push zero.
! Logical NOT: Pop a value. If the value is zero, push 1; otherwise, push zero.
` (backtick) Greater than: Pop a and b, then push 1 if b>a, otherwise push zero.
> Start moving right.
< Start moving left.
^ Start moving up.
v Start moving down.
? Start moving in a random cardinal direction.
_ Pop a value; move right if value = 0, left otherwise.
| Pop a value; move down if value = 0, up otherwise.
" Start string mode: push each character's ASCII value all the way up to the next ".
: Duplicate value on top of the stack. If there is nothing on top of the stack, push a 0.
\ Swap two values on top of the stack. If there is only one value, pretend there is an extra 0 on bottom of the stack.
$ Pop value from the stack and discard it.
. Pop value and output as an integer.
, Pop value and output the ASCII character represented by the integer code that is stored in the value.
# Trampoline: Skip next cell.
p A "put" call (a way to store a value for later use). Pop y, x and v, then change the character at the position (x,y) in the program to the 
character with ASCII value v.
g A "get" call (a way to retrieve data in storage). Pop y and x, then push ASCII value of the character at that position in the program.
@ End program.
  (i.e. a space) No-op. Does nothing.
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