import sys




def load(filename):
    with open(filename) as f:
        return f.read().strip()
    
    
def gen_disk(disk_map):
    id = 0
    map_list = list(disk_map)
    disk = []
    while map_list:
        disk.append((id,int(map_list.pop(0))))
        id += 1
        if map_list:
            c = int(map_list.pop(0))
            if c:
                disk.append((-1, c)) 
    return id-1,disk    

def find_id_idx(disk, id):
    right = len(disk)-1
    while disk[right][0] != id: right -= 1
    return right

def find_space_idx(disk, size, right):
    for idx in range(0,right):
        if disk[idx][0] == -1 and disk[idx][1] >= size:
            return idx
    return 0    

disk_map = load("puzzle.txt")
max_id, disk = gen_disk(disk_map)

print(max_id, disk)

right_idx = len(disk)
print(disk)
for id in range(max_id,0,-1):
    right_idx = find_id_idx(disk,id)
    space_idx = find_space_idx(disk,disk[right_idx][1] ,right_idx)
    if space_idx > 0:
        print(id,space_idx, right_idx)
        disk[right_idx] = (-1,disk[right_idx][1])
        disk[space_idx] = (id,disk[space_idx][1])
        free = disk[space_idx][1] - disk[right_idx][1]
        if free:
            disk[space_idx] = (disk[space_idx][0],disk[right_idx][1])
            disk.insert(space_idx+1, (-1, free))

print(disk)   
defrag = []
for id,size in disk:
    if id == -1:
        id = 0
    defrag.extend([id] * size)
print(defrag)  

chksum = 0
for idx,id in enumerate(defrag):
    chksum += idx*id

print(chksum)    