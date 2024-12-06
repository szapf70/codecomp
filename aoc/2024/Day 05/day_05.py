import sys




def load_data(fname):
    rules = []
    updates = []
    r_flag = True
    with open(fname) as f:
        rules, updates = f.read().split('\n\n')
        rules = list(map(lambda t: (int(t[0]),int(t[1])), list(map(lambda r: tuple(r.split('|')), rules.splitlines()))))
        updates = list(map(lambda t: [int(e) for e in t], list(map(lambda r: r.split(','), updates.splitlines()))))
    return (rules, updates)    

def check_update(update, rules):
    for f,s in rules:
        if f in update and s in update:
            fi, si = update.index(f), update.index(s)
            if si < fi:
                return False
    return True        

def repair_update(update, rules):
    lupdate = update.copy()
    for f,s in rules:
        if f in lupdate and s in lupdate:
            fi, si = lupdate.index(f), lupdate.index(s)
            if si < fi:
                lupdate[fi], lupdate[si] = lupdate[si], lupdate[fi]  
                break 
                     
    return lupdate
           
rules, updates = load_data('day_05.txt')        

num_cor = 0

uo_updates = []
for update in updates:
    if not check_update(update,rules):
        uo_updates.append(update)



for update in uo_updates:
    lupdate = update.copy()
    while True:
        if check_update(lupdate,rules):
            num_cor += lupdate[len(lupdate)//2]  
            break         
        else:
            lupdate = repair_update(lupdate,rules) 
    


        
print("Part 01: ", num_cor)        