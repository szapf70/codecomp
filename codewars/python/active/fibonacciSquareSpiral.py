# https://www.codewars.com/kata/6308dd81a725a9003d75cbd3/train/python
# ASCII Fibonacci Square Spiral

c = [' ', '│', '─', '┌', '┐', '┘', '└', '┤', '├', '┴', '┬', '\n']
    
def square_gen(sq):
    return "\n".join(["".join(row) for row in sq])

def expand(sq,dir):
    match dir:
        case 'E':
            sq[0][-1] = '┬'
            sq[-1][-1] = '┴'
            sq[0] = sq[0] + ['─'] * (2*(len(sq)-1)) + ['┐']
            for i,l in enumerate(sq[1:-1], start=1):
                sq[i] = sq[i] +  [' ' for _ in range(2*(len(sq)-1))] + ['│']
            sq[-1] = sq[-1] + ['─'] * (2*(len(sq)-1)) + ['┘']
                
        case 'S':
            sq[-1][0] = '├'   
            sq[-1][-1] = '┤'
            for _ in range(len(sq)):
                sq.append(['│'] + [' ' for _ in range(len(sq[0])-2)] + ['│'])
            sq.append(['└'] + ['─' for _ in range(len(sq[0])-2)] + ['┘'])    
        case 'W':
            sq[0][0] = '┬'
            sq[-1][0] = '┴'
            sq[0] = ['┌'] + ['─'] * (len(sq)+1) + sq[0]
            for i,l in enumerate(sq[1:-1], start=1):
                sq[i] =  ['│'] +  [' ' for _ in range(len(sq)+1)] + sq[i]
            sq[-1] =  ['└'] + ['─'] * (len(sq)+1) + sq[-1]
        case 'N':
            sq[0][0] = '├'
            sq[0][-1] = '┤'        
            for _ in range(len(sq)-1):
                sq.insert(0,['│'] + [' ' for _ in range(len(sq[0])-2)] + ['│'])
            sq.insert(0,['┌'] + ['─' for _ in range(len(sq[0])-2)] + ['┐'])    
    return sq            

def fibonacci_string(n):
    print(n)
    sq = [['┌','─','┐'],
      ['└','─','┘']]

    d = 'ENWS'
    while n:
        sq = expand(sq, d[0])
        n -= 1
        d = d[1:] + d[0]
    return square_gen(sq)   
    
print(fibonacci_string(4))