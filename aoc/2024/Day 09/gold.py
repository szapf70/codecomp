import sys




def load(filename):
    with open(filename) as f:
        return f.read().strip()
    
    
def gen_disk(disk_map):
    id = 0
    map_list = list(disk_map)
    disk = []
    while map_list:
        disk += [[id] * int(map_list.pop(0))]
        id += 1
        if map_list:
            c = int(map_list.pop(0))
            if c:
                disk += [[-1] * c]
    return disk    
    
def insert_file(spacer, file):
    if len(spacer) == len(file):
        return file
    else:
        return file, spacer[len(file):]    
    
disk_map = load("showcase 01.txt")
disk = gen_disk(disk_map)

print(disk)
free_blocks =[(idx,len(ids)) for idx, ids in enumerate(disk) if ids[0] == -1 ]
print(free_blocks)

sys.exit()

right_idx = len(disk)-1

while right_idx:
    if disk[right_idx][0] == -1:
        right_idx -= 1
        continue
    else:
        for left_idx in range(right_idx):
            if disk[left_idx][0] > 0:
                continue 
            if len(disk[left_idx]) >= len(disk[right_idx])    
        
        
        else:
            


        if disk[e_idx][0] == -1 and len(disk[e_idx]) >= len(disk[idx]):




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
