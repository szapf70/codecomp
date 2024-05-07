# https://www.codewars.com/kata/58e24788e24ddee28e000053
# Simple assembler interpreter

def simple_assembler(program):
    lpr = []
    for ins in program:
        p = ins.split()
        if p[0] == 'mov':
            if p[2].isalpha():
                lpr.append((5,p[1],p[2]))
            else:
                lpr.append((1,p[1],int(p[2])))    
        if p[0] == 'inc':
            lpr.append((2, p[1])) 
        if p[0] == 'dec':
            lpr.append((3, p[1])) 
        if p[0] == 'jnz':
            if p[1].isalpha() and p[2].isalpha():
                lpr.append((6,p[1],p[2]))
            if p[1].isalpha() and not p[2].isalpha():
                lpr.append((7,p[1], int(p[2])))
            if not p[1].isalpha() and p[2].isalpha():
                lpr.append((8,int(p[1]), p[2]))
            if not p[1].isalpha() and not p[2].isalpha():
                lpr.append((9, int(p[1]), int(p[2])))                     

    pc = 0
    regs = {}
    while pc < len(lpr):
        p = lpr[pc]
        match p[0]:
            case 1:
                regs[p[1]] = p[2]
                pc += 1
                continue
            case 5:
                regs[p[1]] = regs[p[2]]
                pc += 1
                continue
            case 2:
                regs[p[1]] += 1
                pc += 1
                continue
            case 3:
                regs[p[1]] -= 1
                pc += 1
                continue
            case 6:
                if regs[p[1]] != 0:
                    pc += regs[p[2]]
                    continue
                pc += 1
                continue
            case 7:
                if regs[p[1]] != 0:
                    pc += p[2]
                    continue    
                pc += 1
                continue
            case 8:
                if p[1] != 0:
                    pc += regs[p[2]]
                    continue
                pc += 1
                continue
            case 9:
                if p[1] != 0:
                    pc += p[2] 
                    continue
                pc += 1
                continue       
    return regs


#print(simple_assembler(["mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a"]))    
print(simple_assembler(['mov c 12', 'mov b 0', 'mov a 200', 'dec a', 'inc b', 'jnz a -2', 'dec c', 'mov a b', 'jnz c -5', 'jnz 0 1', 'mov c a']))    


"""This is the first part of this kata series. Second part is here.

We want to create a simple interpreter of assembler which will support the following instructions:

mov x y - copies y (either a constant value or the content of a register) into register x
inc x - increases the content of the register x by one
dec x - decreases the content of the register x by one
jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant), 
but only if x (a constant or a register) is not zero Register names are alphabetical (letters only). Constants are always integers 
(positive or negative).

Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of the program instructions and will execute them. The program ends when there are no more instructions to execute, then it returns a dictionary (a table in COBOL) with the contents of the registers.

Also, every inc/dec/jnz on a register will always be preceeded by a mov on the register first, so you don't need to worry about uninitialized registers."""