# https://www.codewars.com/kata/57d7536d950d8474f6000a06/train/python
# The Wrong-Way Cow

def find_wrong_way_cow(field):
    dirs = {'up' : [], 'down' : [], 'left' : [], 'right' : []}
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == 'c':
                # down
                if y < len(field)-2 and field[y+1][x] == 'o' and field[y+2][x] == 'w':
                    dirs['down'].append([x,y])
                # up
                if y > 1 and field[y-1][x] == 'o' and field[y-2][x] == 'w':
                    dirs['up'].append([x,y])
                # right
                if x < len(field[0])-2 and field[y][x+1] == 'o' and field[y][x+2] == 'w':
                    dirs['right'].append([x,y])
                # left    
                if x > 1 and field[y][x-1] == 'o' and field[y][x-2] == 'w':
                    dirs['left'].append([x,y])

    for c in dirs:
        if len(dirs[c]) == 1:
            return dirs[c][0]



field1 = list(map(list, ["cow.cow.cow.cow.cow",
                         "cow.cow.cow.cow.cow",
                         "cow.woc.cow.cow.cow",
                         "cow.cow.cow.cow.cow"]))
                                
print(find_wrong_way_cow(field1), [6,2])
        
        
field2 = list(map(list, ["c..........",
                         "o...c......",
                         "w...o.c....",
                         "....w.o....",
                         "......w.cow"]))
                                
print(find_wrong_way_cow(field2), [8,4])