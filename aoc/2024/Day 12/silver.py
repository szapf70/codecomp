




def load(filename):
    garden = {}
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                garden[(x,y)] = lines[y][x]
    return garden




def capture_plot(garden):








garden = load('showcase 01.txt')
print(garden)

while garden:
