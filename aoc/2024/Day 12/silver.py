import sys




def load(filename):
    garden = {}
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                garden[(x,y)] = lines[y][x]
    return garden





def capture_plot(garden, x,y,t,plot):
    def neighbors(garden,x,y,t):
        _nl = []
        for xn,yn in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
            if (xn,yn) in garden and garden[(xn,yn)] == t and (xn,yn) not in plot['seen']:
                _nl.append((xn,yn))
        return _nl        

    nl = neighbors(garden,x,y,t)
    if not nl:
        

garden = load('showcase 01.txt')
plots = []


while garden:
    plot = {'area' : 0,
           'perimeter' : 0,
           'seen' : set()}
    (x,y),t = garden.popitem()
    capture_plot(garden,x,y,t,plot)

    break