# https://www.codewars.com/kata/591d0fd7c09ee0021400005b/train/python
# Simple Fun #289: Sum The Difference

def sum_the_difference(equation):
    eq = " " + equation.replace(" ", "")
    e = 0
    o = 0
    for i in range(len(eq)):
        if eq[i] in "2468":
            e += -int(eq[i]) if eq[i-1] == "-" else int(eq[i])
        if eq[i] in "13579":
            o += -int(eq[i]) if eq[i-1] == "-" else int(eq[i])
    return e - o

print(sum_the_difference("(-100) + 100  - (-200) + 1)"))