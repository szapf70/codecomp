# Helper für Total area covered by rectangles
# https://www.codewars.com/kata/55dcdd2c5a73bdddcb000044/train/python
# 

def isSeperate(r1,r2):
    if r1[2] <= r2[0] or r2[2] <= r1[0]:
        return True
    if r1[3] <= r2[1] or r2[3] <= r1[1]:
        return True
    return False

def isR1InsideR2(r1,r2):
    return r2[0] <= r1[0] and r2[1] <= r1[1] and r2[2] >= r1[2] and r2[3] >= r1[3]




def getOverlap(r1,r2):
    return ( max(r1[0],r2[0]), max(r1[1],r2[1]),
             min(r1[2],r2[2]), min(r1[3],r2[3]) )

def cutRect(r,c):
    if (r[0],r[1]) == (c[0],c[1]):
        # c liegt vorne/unten
        if (c[2] < r[2]):
            # vorne
            return (c[2],c[1],r[2],r[3])
        else:
            # unten
            return (c[0],c[3],r[2],r[3])    
    else:
        # c liegt hinten/oben
        if (c[0] > r[0]):
            #hinten
            return (r[0],r[1],c[0],c[3])
        else:
            # oben
            return (r[0],r[1],c[2],c[1])    

#print(getOverlap((3,3,8,5),(6,3,8,9)))
#print(cutRect((3,3,8,5),(6,3,8,5)))
#print(getOverlap((0,0,20,20),(5,5,25,25)))
#print(getOverlap((40,2,60,40),(50,25,70,35)))



def calculate(rects):
    # First eliminate those who not overlap 
    print("Eingabe:",rects)
    rlist = []
    olist = []
    area = 0
    # Durchgang 1. alle Rechtecke die nicht überlappen löschen und die Fläche zum Ergebnis addieren.
    for i in range(len(rects)):
        allsep = True
        for j in range(len(rects)):
            if i!=j:
                # Überlappung, überdeckung?
                if not isSeperate(rects[i],rects[j]):
                    allsep = False
                    if isR1InsideR2(rects[j],rects[i]):
                        
                    rlist.append(rects[i])

                    break
        if allsep:
            area += (rects[i][2]-rects[i][0])*(rects[i][3]-rects[i][1])
    print("Nach Durchgang 1:",rlist,area)
    # Durchgang 2. alle Rectecke löschen die komplett durch ein anders überdeckt werden
    




r = [(3,3,8,5),(6,3,8,9),(11,6,14,12)]

print(calculate(r))