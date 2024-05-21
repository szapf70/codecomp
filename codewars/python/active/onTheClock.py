# https://www.codewars.com/kata/5d629a6c65c7010022e3b226/train/python
# On the clock


def decimal_time(tStr):
    h,m = [int(i) for i in tStr[:-2].split(':')]
    am = tStr[-2:] == 'am'
    if am and h == 12: h = 0
    if h and not am: h += 12
     # minutes
    for f,t,r in [(0,7,0.0),(8,22,0.25),(23,37,0.5),(38,52,0.75),(53,59,1.0)]:
        if f <= m <= t:
            h += r    
    return h    
        
def get_hours(shifts):
    res = []
    for s in shifts:
        res.append(decimal_time(s[1])-decimal_time(s[0]))
    return res

#print(decimal_time("03:23am"))


print(get_hours([("2:00pm", "8:00pm"), ("8:00am", "4:30pm")]), [6.0, 8.5])
print(get_hours([("5:02am", "2:30pm"), ("10:00pm", "3:00am")]), [9.5, 5.0])
print(get_hours([("1:41pm", "6:50pm")]), [5.25])
print(get_hours([("12:01am", "3:00am"), ("3:00pm", "12:00pm")]), [3.0, 21.0])