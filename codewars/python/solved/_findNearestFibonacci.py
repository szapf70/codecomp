# https://www.codewars.com/kata/5ca22e6b86eed5002812061e/train/python
# Find Nearest Fibonacci Number

fb = [0,1,1,2,3,5,8,13,21,34]
    
def nearest_fibonacci(number):
    while fb[-1] <= number:
        fb.append(fb[-1]+fb[-2])
    fb.append(fb[-1]+fb[-2])

    idx = 0

    while fb[idx] < number:
        idx += 1
    if fb[idx] == number:
        return fb[idx]
    pre = number - fb[idx-1]
    post = fb[idx] - number
    if pre <= post:
        return fb[idx-1]
    return fb[idx]

print(nearest_fibonacci(54))
