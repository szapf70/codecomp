# https://www.codewars.com/kata/6308dd81a725a9003d75cbd3/train/python
# ASCII Fibonacci Square Spiral
# A square with sidelength m is always 2*m+1 characters wide and m+1 characters high.

c = [' ', '│', '─', '┌', '┐', '┘', '└', '┤', '├', '┴', '┬', '\n']
fib = [1,1]

def gen_square(slen):
    eh = slen - 1
    ew = 2 * slen -1
    sq = [] 
    sq.append(['┌'] + ['─'] * (ew) + ['┐']) 
    for _ in range(eh):
        sq.append(['│'] + [' '] * (ew) + ['│'])       
    sq.append(['└'] + ['─'] * (ew) + ['┘']) 
    return sq  

    
def square_str(sq):
    return "\n".join(["".join(row) for row in sq])

def expand(sq,dir,side):
    gs = gen_square(side)
    match dir:
        case 'E':
            sq[0][-1] = '┬'
            sq[-1][-1] = '┴'
            for i,r in enumerate(sq):
                sq[i] = sq[i] + gs[i][1:]

        case 'W':
            sq[0][0] = '┬'
            sq[-1][0] = '┴'
            for i,r in enumerate(sq):
                sq[i] = gs[i][:-1] + sq[i]

        case 'S':
            sq[-1][0] = '├'   
            sq[-1][-1] = '┤'
            for r in gs[1:]:
                sq.append(r)

        case 'N':
            sq[0][0] = '├'
            sq[0][-1] = '┤'        
            for r in gs[:-1][::-1]:
                sq.insert(0,r)

    return sq            

def fibonacci_string(n):
    while n >= len(fib):
        fib.append(fib[-1] + fib[-2])
    
    sq = [['┌','─','┐'],
          ['└','─','┘']]

    d = 'ENWS'
    fpos = 1
    while n:
        sq = expand(sq, d[0],fib[fpos])
        n -= 1
        fpos += 1
        d = d[1:] + d[0]
    return square_str(sq)   
    
print(fibonacci_string(5))
print(fib)
