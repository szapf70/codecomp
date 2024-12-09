import sys




def load(filename):
    with open(filename) as f:
        return f.read().strip()
    
    
def gen_disk(disk_map):
    id = 0
    map_list = list(disk_map)
    disk = []
    while map_list:
        disk += [id] * int(map_list.pop(0))
        id += 1
        if map_list:
            disk += [-1] * int(map_list.pop(0))
    return disk    
    
disk_map = load("puzzle.txt")
disk = gen_disk(disk_map)

print(disk)



free_blocks =[idx for idx, id in enumerate(disk) if id == -1 ]
print(free_blocks)

#sys.exit()


while free_blocks:
    #print(disk,free_blocks)

    id = disk.pop()
    if id != -1:
        free_idx = free_blocks.pop(0)
        if free_idx < len(disk):
            disk[free_idx] = id
    else:
        free_blocks.pop()

#print(disk,free_blocks)


chksum = 0
for idx,id in enumerate(disk):
    chksum += idx * id

print(chksum)
