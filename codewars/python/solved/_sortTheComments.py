# https://www.codewars.com/kata/58a0f18091e53d2ad1000039/train/python
# Sort the comments!


def sort_ranks(ranks):
    nr = []
    ml = 0 
    for r in ranks:
        rr = ".".join([p.rjust(5,'0') for p in r.split('.')])
        nr.append((rr,r))
    return [e[1] for e in sorted(nr)]


