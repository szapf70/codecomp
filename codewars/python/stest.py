def is_merge(s, part1, part2):
    if sorted(s) == sorted(part1+part2):
        p1c = list(part1)
        for l in s:
            if l == p1c[0]:
                p1c.pop(0)
                if len(p1c) == 0: break        
        if len(p1c) > 0: return False
        p2c = list(part2)
        for l in s:
            if l == p2c[0]:
                p2c.pop(0)
                if len(p2c) == 0: break        
        if len(p2c) > 0: return False
        return True


    else:
         return False    



print(is_merge('codewars', 'code', 'wars')) #, True
print(is_merge('codewars', 'cdw', 'oears')) # ,True)
print(is_merge('codewars', 'cod', 'wars')) # ,False)