# https://www.codewars.com/kata/56548dad6dae7b8756000037/train/python
# Clock in Mirror


def what_is_the_time(time_in_mirror):
    h = int(time_in_mirror.split(':')[0])
    m = int(time_in_mirror.split(':')[1])
    if m != 0 and m!= 30: m = 60 - m
    h  = 11 - h
    return str(h).rjust(2,"0") + ":" + str(m).rjust(2, "0")

#print(what_is_the_time("05:25"))
#print(what_is_the_time("06:35"))

def t(tim):
    h = int(tim.split(':')[0])
    m = int(tim.split(':')[1])
    if m != 0 and m!= 30: m = 60 - m

    if h < 6:
        h = 6 + (h-6+1)
    else:
        h = 6 - (h-1+6)    
    
    
    return h,m


print(t("04:00"))
print(t("08:00"))


"""
in the same manner:

05:25 --> 06:35

01:50 --> 10:10

11:58 --> 12:02

12:01 --> 11:59

Please complete the function WhatIsTheTime(timeInMirror), where timeInMirror is the mirrored time (what Peter sees) as string.

Return the real time as a string.

Consider hours to be between 1 <= hour < 13.

So there is no 00:20, instead it is 12:20.

There is no 13:20, instead it is 01:20.


"""