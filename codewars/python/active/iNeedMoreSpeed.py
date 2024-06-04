# https://www.codewars.com/kata/55de9c184bb732a87f000055/train/python
# I need more speed!

def reverse(seq):
    for i in range(len(seq)//2+1):
        seq[i], seq[(len(seq)-1)-i] = seq[(len(seq)-1)-i], seq[i]


s = [1,2,3,4,5,6]

print(s)
reverse(s)
print(s)