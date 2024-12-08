#





def solveable(equ):
    res, nums = equ
    steps = []
    steps.append([nums.pop(0)])
    while nums:
        num = nums.pop(0)
        l_steps = []
        for sn in steps[-1]:
            l_steps.append(sn+num)
            l_steps.append(sn*num)
        steps.append(l_steps.copy())    
    return res in steps[-1]    


equations = []

with open('day_07.txt') as f:
    for line in f:
        res, nums = line.split(': ')
        equations.append((int(res),list(map(int, nums.split()))))

#print(equations)        

solve_ctr = 0
solve_sum = 0

for eq in equations:
    if solveable(eq):
        solve_sum += eq[0]
        solve_ctr += 1

print(solve_ctr, solve_sum)        
