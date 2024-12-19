# https://www.codewars.com/kata/5672f4e3404d0609ec00000a/train/python
# Create a frame!

def frame(text, char):
    _max = max([len(_l) for _l in text])
    text = list(map(lambda t: t.ljust(_max), text))
    res = []
    res.append(char * (_max + 4))
    for _l in text:
        res.append(char + ' ' + _l + ' ' + char)
    res.append(char * (_max + 4))
    return "\n".join(res)


def frame2(text, char):
    n = len(max(text, key=len)) + 4
    return "\n".join( [char * n] +
                      ["%s %s %s" % (char, line.ljust(n-4), char) for line in text] +
                      [char * n] )






print(frame(['Small', 'frame'], '~'),
    """~~~~~~~~~
~ Small ~
~ frame ~
~~~~~~~~~""")

print(frame(['Create','this','kata'], '+'),
    """++++++++++
+ Create +
+ this   +
+ kata   +
++++++++++""")

print(frame(['This is a very long single frame'], '-'),
    """------------------------------------
- This is a very long single frame -
------------------------------------""")
