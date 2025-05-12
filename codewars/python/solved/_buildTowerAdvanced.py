# https://www.codewars.com/kata/57675f3dedc6f728ee000256/train/python
# Build Tower Advanced

def tower_builder(n_floors, block_size):
    _tower = []
    w, h = block_size
    for n in range(1,n_floors+1):
        _bl = ' ' * (w*(n_floors-n)) + '*' * (w*(2*n-1)) + ' ' * (w*(n_floors-n))
        for _ in range(h):
            _tower.append(_bl)
    return _tower


print(tower_builder(1, (1, 1)), ['*', ])
print(tower_builder(3, (4, 2)), ['        ****        ', '        ****        ', '    ************    ', '    ************    ', '********************', '********************'])