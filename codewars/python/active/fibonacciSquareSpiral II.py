# https://www.codewars.com/kata/6308dd81a725a9003d75cbd3/train/python
# ASCII Fibonacci Square Spiral

c = [' ', '│', '─', '┌', '┐', '┘', '└', '┤', '├', '┴', '┬', '\n']
fib = [1,1,2,3,5,8,13]


    
def square_gen(sq):
    return "\n".join(["".join(row) for row in sq])

def expand(sq,dir,side):
    match dir:
        case 'E':
            ################################
            sq[0]  = sq[0][:-1]  + ['┬'] + ['─'] * (2*fib[side]-1) + ['┐']
            for i,r in enumerate(sq[1:-1],start=1):
                sq[i] = sq[i] + [' '] * (2*fib[side]-1) + ['│']
            sq[-1] = sq[-1][:-1] + ['┴'] + ['─'] * (2*fib[side]-1) + ['┘']
            ################################    
        case 'S':
            sq[-1][0] = '├'   
            sq[-1][-1] = '┤'
        case 'W':
            sq[0][0] = '┬'
            sq[-1][0] = '┴'
        case 'N':
            sq[0][0] = '├'
            sq[0][-1] = '┤'        
    return sq            

def fibonacci_string(n):
    while n > len(fib):
        fib.append(fib[-1] + fib[-2])
    
    sq = [['┌','─','┐'],
          ['└','─','┘']]

    d = 'ENWS'
    fpos = 1
    while n:
        sq = expand(sq, d[0],fpos)
        n -= 1
        d = d[1:] + d[0]
    return square_gen(sq)   
    
print(fibonacci_string(2))