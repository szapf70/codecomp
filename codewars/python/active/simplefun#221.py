# https://www.codewars.com/kata/5902bc48378a926538000044/train/python
# Simple Fun #221: Furthest Distance Of Same Letter

def dist_same_letter(st):
    cnt = {}
    res = []
    for i,l in enumerate(st):
        if not l in cnt.keys():
            cnt[l] = i
        else:
            res.append((i - cnt[l],i, l))    
    #res = sorted(res, reverse = True)
    res = sorted(res, reverse = True, key = lambda x: (x[0], -x[1]))
    return res[0][2] + str(res[0][0]+1)


print(dist_same_letter("fffffahhhhhhaaahhhhbhhahhhhabxx"),"a23")
print(dist_same_letter("ucabcabcabcdfxhuizfgrsuixacbcx"),"c28")
print(dist_same_letter("iaufzhaifxhuzofghabcbacdbuzoxih"),"i30")
print(dist_same_letter("axaxfaaiiiofizxuiox"),"x18")
print(dist_same_letter("fxfaufhacaaacaaabbbabaddb"),"a19")
print(dist_same_letter("fxauf"),"f5")