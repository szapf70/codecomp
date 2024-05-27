def robot_walk(arr):
    print(arr)
    y,x  = 0,0
    d = ['u','r','d','l']
    seen = set()
    seen.add((0,0))
    for step in arr:
        for s in range(step):
            if d[0] == 'u': y += 1
            if d[0] == 'r': x += 1
            if d[0] == 'd': y -= 1
            if d[0] == 'l': x -= 1
            if (y,x) in seen: return True
            seen.add((y,x))
            print(y,x,seen)
        d.append(d.pop(0))
    return False
   

print(robot_walk([5,5,5,5]),False)
