from math import lcm
input = open("input.txt").read().strip()
instructions, rest = input.split('\n\n')

nodes = {line.split(' = ')[0]: line.split(' = ')[1][1:-1].split(', ') for line in rest.split('\n')}

def traverse_p1(start, end):
    i, steps = 0, 0
    while start != end:
        if i == len(instructions): i = 0
        start = nodes[start][0] if instructions[i] == 'L' else nodes[start][1]
        steps += 1
        i += 1
    return steps
part1 = traverse_p1('AAA', 'ZZZ')
print(part1)

def traverse_p2(start):
    i, steps = 0, 0
    while not start.endswith('Z'):
        if i == len(instructions): i = 0
        start = nodes[start][0] if instructions[i] == 'L' else nodes[start][1]
        steps += 1
        i += 1
    return steps

starts = [start for start in nodes if start.endswith('A')]
part2 = 1
for start in starts:
    part2 = lcm(part2, traverse_p2(start))
print(part2)