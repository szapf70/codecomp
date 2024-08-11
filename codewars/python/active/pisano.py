fb = [0,1,1,2,3,5,8,13,21]

while len(fb) <= 60:
    fb += [fb[-1]+fb[-2]]

fbs = [(i**2)%10 for i in fb]
print(fbs)