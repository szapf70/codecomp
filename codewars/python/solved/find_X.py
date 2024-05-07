# https://www.codewars.com/kata/5ae71f8c2c5061059e000044/train/python
# Find X

# optimize
def find_x_old(n):
    x = 0
    for i in range(n):
        for j in range(2*n):
            print(i,j)
            x += i+j
    return x

#  (n × ( n + 1))/2

def find_x(n):
    n1 = n-1
    s1 = 2*n * ((n1 * (n1 + 1))/2)
    n2 = 2*n-1
    s2 = n * ((n2*(n2+1))/2)    
    return int(s1 + s2)



print(find_x_old(3))
print(find_x(3))