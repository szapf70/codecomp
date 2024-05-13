# https://www.codewars.com/kata/6638277786032a014d3e0072/train/python
# Allocating Hotel Rooms

def allocate_rooms(customers):
    customers = sorted(customers)
    rooms = []
    res = []
    for cst in customers:
        if rooms == []:
            rooms.append(cst[1])
            res.append(1)
            continue
        booked = False
        for ridx in range(len(rooms)):
            if rooms[ridx] < cst[0]:
                rooms[ridx] = cst[1]
                res.append(ridx+1)
                booked = True
                break
        
        if not booked:
            rooms.append(cst[1])  
            res.append(len(rooms))  
    
    ## Write code here
    return res


#print(allocate_rooms([(1,2),(2,4),(4,4)]))
print(allocate_rooms([(1,5),(2,4),(6,8),(7,7)]))
#print(allocate_rooms([(15,22),(2,4),(6,9),(3,33),(12,21)]))
  