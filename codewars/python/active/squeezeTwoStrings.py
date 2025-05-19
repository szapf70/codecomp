# https://www.codewars.com/kata/57d7935d1a6282fa28000041/train/python
# Squeeze two Strings

def squeeze(left, right):
    lstr = [s.rstrip() for s in left.splitlines()]
    rstr = [s.lstrip() for s in right.splitlines()]
    while len(lstr) != len(rstr):
        if len(lstr) < len(rstr):
            lstr.append("")
        else:
            rstr.append("")    
    mlmax = max([len(l) + len(r) for l,r in zip(lstr,rstr)])
    res = [l + (" " * (mlmax-(len(l)+len(r)))) + r for l,r in zip(lstr,rstr)]
    return "\n".join([r.rstrip() for r in res])



left = """aaaaaaaa       
bbb            
cccccc         
dd             
eeeeeeeeeeeeeee"""

right = """       fff
   ggggggg
      hhhh
iiiiiiiiii
      jjjj"""

answer = """aaaaaaaa        fff
bbb         ggggggg
cccccc         hhhh
dd       iiiiiiiiii
eeeeeeeeeeeeeeejjjj"""

print(squeeze(left,right))