


with open("input.txt", "r") as txt:
    cal_sum = 0
    for cal_line in txt.readlines():
        nums = [c for c in cal_line if c.isdigit()]
        cal_sum += int(nums[0] + nums[-1])
    print(cal_sum)

