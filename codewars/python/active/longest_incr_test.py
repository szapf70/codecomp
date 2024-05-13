



def find_longest_incr(arr):
    
    idx = 2
    run = False
    
    top = {'l' : 0, 's' : 0, 'e' : 0}
    act = {'l' : 0, 's' : 0, 'e' : 0}
    
    while idx < len(arr):
        if not run:    
            # Startet ein run?
            if arr[idx-2] < arr[idx-1] < arr[idx]:
                # Drei aufsteigende, run startet, act wird initialsiert
                run = True
                act.update({'l' : 2,'s' : idx-2, 'e' : idx})
                # run verfolgen
                while run:
                    print(act)
                    idx += 1
                    # ende des arrays, run noch aktiv?    
                    if idx == len(arr):
                        if act['l'] > top['l']:
                            top.update(act)
                            run = False
                            break
                    else:
                        # run läuft weiter, länge und ende akt.
                        if arr[idx] > arr[idx-1]:
                            act['l'] += 1
                            act['e'] += 1
                        # run läuft nicht weiter, wenn aktueller run länger, dann neue top setzen
                        else:
                            run = False
                            if act['l'] > top['l']:
                                top.update(act)
            else:    
                idx += 1        
        
    return top





arr1 = [345, 32, 45, 12, 45, 47, 49, 55, 90, 104, 20, 30, 34]
arr2 = [345,  20, 30, 34,32, 45, 12, 45, 47, 49, 55, 90, 104]
arr3 = [10,9,8,7,6,5,4,3,2,1]

print(find_longest_incr(arr1))
print(find_longest_incr(arr2))

