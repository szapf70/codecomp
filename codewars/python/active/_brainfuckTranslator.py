# https://www.codewars.com/kata/58924f2ca8c628f21a0001a1/train/python
# Brainfuck Translator


def preprocess(sc):
    ret = []
    last = None
    for c in sc:
        if c in '.,[]':
            ret.append(c)
            last = None
            continue
        if c in '+-<>':
            if last == None or last != c:
                ret.append(c)
                last = c
            else:
                ret[-1] += c    
    return ret

def brainfuck_to_c(source_code):
    # tidy up
    sc = ''.join([c for c in source_code if c in '+-<>,.[]'])
    while True:
        bef = len(sc)
        for p in ['+-', '-+','<>','><','[]']:
            sc = sc.replace(p, '')
        if bef == len(sc):
            break

    # Check for unpaired braces
    blevel = 0
    for c in sc:
        if c == '[': blevel += 1
        if c == ']': blevel -= 1
        if blevel < 0:
            break
    if blevel != 0:
        return "Error!"    

    # Preprocess
    tk = preprocess(sc)

    # Output
    idlvl = 0
    out_str  =""
    for t in tk:
        idstr = " " * idlvl
        match t[0]:
            case '.':
                idstr += 'putchar(*p);\n'
            case ',':
                idstr += '*p = getchar();\n'
            case '[':
                idstr += 'if (*p) do {\n'
                idlvl += 2
            case ']':
                idstr = idstr[:-2] + '} while (*p);\n' 
                idlvl -= 2
            case '+':
                idstr += f'*p += {len(t)};\n'
            case '-':           
                idstr += f'*p -= {len(t)};\n'
            case '>':
                idstr += f'p += {len(t)};\n'
            case '<':
                idstr += f'p -= {len(t)};\n'    
    
        out_str += idstr
    
    return out_str

#print(preprocess(">>>>+++++[>----..]"))
print(brainfuck_to_c('[>>[<<]]'))
#print(brainfuck_to_c('++--+.'))
#print(brainfuck_to_c('[][+++]'))
#print(brainfuck_to_c('<>><'))