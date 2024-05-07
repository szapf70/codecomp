import sys

def average_string(s):
    if len(s) == 0 : return "n/a"
    nums = ["zero", "one", "two", "three", "four",
            "five" ,"six" , "seven" , "eight", "nine"]
    ns = s.split()
    sum = 0
    for n in ns:
        if n in nums:
            sum += nums.index(n)   
        else:
            return "n/a"
    return nums[int(sum/len(ns))]  

print(average_string("zero nine five two"))#, "four")
print(average_string("four six two three"))#, "three")
print(average_string("one two three four five"))#, "three")
print(average_string("five four"))#, "four")
print(average_string("zero zero zero zero zero"))#, "zero")
print(average_string("one one eight one"))#, "two")
print(average_string("one"))#, "one")
print(average_string(""))#, "n/a")
print(average_string("ten"))#, "n/a")
print(average_string("pippi"))#, "n/a")