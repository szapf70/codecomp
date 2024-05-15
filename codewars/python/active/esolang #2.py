# https://www.codewars.com/kata/58678d29dbca9a68d80000d7/train/python
# Esolang Interpreters #2 - Custom Smallfuck Interpreter

def interpreter(code, tape):
    carr, tarr = list(code), list(tape)
    pc = 0
    tp = 0
    sub = 0
    while -1 < pc < len(code) and -1 < tp < len(tape):
        match carr[pc]:
            case '>':
                tp += 1
                pc += 1
            case '<':
                tp -= 1
                pc += 1
            case '*':
                tarr[tp] = '1' if tarr[tp] == '0' else '0'
                pc += 1
            case '[':
                if tarr[tp] == '0':
                    lsub = sub
                    lpc = pc
                    while lpc < len(carr)-1:
                        lpc += 1
                        if carr[lpc] == '[':
                            lsub += 1
                            continue
                        if carr[lpc] == ']':
                            if lsub == sub:
                                pc = lpc+1
                                break
                            if lsub > sub:
                                lsub -= 1
                else:
                    pc += 1                
            case ']':
                if tarr[tp] != '0':
                    lsub = sub
                    lpc = pc 
                    while lpc > 0:
                        lpc -= 1
                        if carr[lpc] == ']':
                            lsub += 1
                            continue                     
                        if carr[lpc] == '[':
                            if lsub == sub:
                                pc = lpc
                                break     
                            if lsub > sub:
                                lsub -= 1  
                else:
                    pc += 1                  
            case _:
                pc += 1    

    return "".join(tarr)


print(interpreter(">*>*", "00101100"), "01001100")
print(interpreter("*>*>*>*>*>*>*>*", "00101100"), "11010011")
print(interpreter("*>*>>*>>>*>*", "00101100"), "11111111")
print(interpreter(">>>>>*<*<<*", "00101100"), "00000000")

"""
Here are a list of commands in Smallfuck:

> - Move pointer to the right (by 1 cell)
< - Move pointer to the left (by 1 cell)
* - Flip the bit at the current cell
[ - Jump past matching ] if value at current cell is 0
] - Jump back to matching [ (if value at current cell is nonzero)



        test.assert_equals(interpreter(">*>*", "00101100"), "01001100")
        # Flips all the bits in the tape
        test.assert_equals(interpreter("*>*>*>*>*>*>*>*", "00101100"), "11010011")
        # Flips all the bits that are initialized to 0
        test.assert_equals(interpreter("*>*>>*>>>*>*", "00101100"), "11111111")
        # Goes somewhere to the right of the tape and then flips all bits that are initialized to 1, progressing leftwards through the tape
        test.assert_equals(interpreter(">>>>>*<*<<*", "00101100"), "00000000")
"""