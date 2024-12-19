# https://www.codewars.com/kata/5898a751b2edc082f60005f4/train/python
# Tombola - validation

def check_tombola(sheet):
	for _r in sheet:
		if len(_r) != 9: return False

	if len(sheet) != 3:
		return False
	
	un = set()
	for _r in sheet:
		_act = set(_r)
	un.remove(0)
	if len(un) != 15:
		return False
		




sheet =  [
[0, 11, 20, 0, 44, 0, 60, 76, 0],
[0, 12, 0, 34, 45, 0, 63, 0, 82],
[2, 0, 27, 0, 48, 51, 66, 0,  0]
]
print(check_tombola(sheet), True)
sheet =  [
[0, 16, 0, 37, 0, 54, 0, 75, 81],
[1, 0, 28, 0, 41, 59, 0, 0, 84],
[0, 19, 29, 0, 45, 0, 65, 0, 89]
]
print(check_tombola(sheet), True)

sheet =  [
[0, 11, 0, 30, 0, 54, 0, 77, 83],
[8, 12, 0, 32, 0, 58, 0, 79, 0],
[0, 13, 29, 0, 40, 0, 67, 0, 90]
]
print(check_tombola(sheet), True)

sheet =  [
[0, 0, 0, 35, 0, 55, 60, 72, 86],
[3, 0, 22, 0, 40, 58, 0, 79, 0],
[7, 0, 25, 0, 41, 0, 65, 0, 88]
]
print(check_tombola(sheet), False)

sheet =  [
[0, 13, 0, 35, 0, 55, 0, 72, 86],
[3, 0, 21, 0, 40, 53, 0, 79, 0],
[7, 0, 29, 0, 41, 0, 65, 0, 88]
]
print(check_tombola(sheet), False)

sheet =  [
[0, 11, 20, 0, 44, 0, 60, 76, 0],
[0, 12, 0, 34, 45, 0, 63, 0, 82],
[2, 0, 27, 0, 48, 51, 63, 0,  0]
]
print(check_tombola(sheet), False)

sheet =  [
[0, 11, 24, 0, 41, 0, 65, 70, 0],
[0, 16, 0, 32, 48, 0, 67, 0, 89],
[0, 0, 0, 0, 0, 0, 67, 0, 89],
[1, 0, 27, 33, 0, 59, 0, 74, 0]
]
print(check_tombola(sheet), False)

sheet =  [
[0, 13, 0, 35, 0, 55, 0, 72, 86],
[3, 0, 25, 0, 40, 58, 0, 79, 0],
[7, 0, 22, 0, 41, 0, 65, 0, 88]
]
print(check_tombola(sheet), False)