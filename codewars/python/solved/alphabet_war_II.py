# https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/python
# Alphabet war - airstrike - letters massacre


def alphabet_war(fight):
    fl = list(fight)
    for i in range(len(fl)):
        if fl[i] == '*':
            if i > 0:
                fl[i-1] = '_'
            fl[i] = '_'
            if i < len(fl)-1:
                if fl[i+1] != '*':
                    fl[i+1] = '_'
    fight = "".join(fl)

    p = {
            "w" : { "side" : "left", "pow" : 4},
            "p" : { "side" : "left", "pow" : 3},
            "b" : { "side" : "left", "pow" : 2},
            "s" : { "side" : "left", "pow" : 1},
            "m" : { "side" : "right", "pow" : 4},
            "q" : { "side" : "right", "pow" : 3},
            "d" : { "side" : "right", "pow" : 2},
            "z" : { "side" : "right", "pow" : 1},
            "left" : 0,
            "right" : 0
        }
    for l in fight:
        if l in p:
            p[p[l]["side"]] += p[l]["pow"]
    if p["left"] > p["right"]: return "Left side wins!"
    if p["left"] < p["right"]: return "Right side wins!"
    return "Let's fight again!"

print(alphabet_war('www*www****z'))