# https://www.codewars.com/kata/543ddf69386034670d000c7d/train/python
# Angle Between Clock Hands




import math

def hand_angle(hours, minutes):
    amh = minutes * 6
    ahh = (hours%12) * 30 + minutes * 0.5
    a = abs(amh-ahh)
    return min(a, 360-a)*(math.pi/180)



print(hand_angle(10,0))

"""		do_test(0, 0, 0)
		do_test(12, 0, 0)
		do_test(6, 0, 180)
		do_test(1, 0, 30)
		do_test(9, 0, 90)
		do_test(10, 0, 60)
		do_test(0, 15, 82.5)
		do_test(0, 45, 112.5)
		do_test(12, 30, 165)
		do_test(7, 15, 127.5)
		do_test(6, 5, 152.5)"""
