
def solveable(equ):
    res, nums = equ
    nums = list(map(int, nums))
    steps = []
    steps.append([nums.pop(0)])
    while nums:
        num = nums.pop(0)
        l_steps = []
        for sn in steps[-1]:
            l_steps.append(sn+num)
            l_steps.append(sn*num)
            l_steps.append(int(str(sn)+str(num)))
        steps.append(l_steps.copy())    
    return res in steps[-1]    


equations = []

with open('day_07.txt') as f:
    for line in f:
        res, nums = line.split(': ')
        equations.append((int(res),nums.split()))

#print(equations)        

solve_sum = 0

for eq in equations:
    if solveable(eq):
        solve_sum += eq[0]
print(solve_sum)        