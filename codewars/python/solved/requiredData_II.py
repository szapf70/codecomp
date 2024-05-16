# https://www.codewars.com/kata/560985a07add63e1a1000019/train/python
# Required Data II (Easy One)

def given_nth_value(arr, k, str_):
    if len(arr) == 0:
        return "No values in the array"
    str_ = str_.lower()
    if not (str_ == 'max' or str_ == 'min'):
        return "Valid entries: 'max' or 'min'"
    for e in arr:
        if type(e) != int:
            return "Invalid entry list"

    pre = sorted(set(arr), reverse = (str_ == 'max'))
    if k > len(pre):
        return "No way"

    return pre[k-1]


arr = [3, 3, -1, 10, 6, 8, -5, 4, 22, 31, 34, - 16, -16, 8 , 8] # (15 elements)
k = 5
str_ = "min"
print(given_nth_value(arr, k, str_), 4)

arr = [3, 3, -1, 10, 6, 8, -5, 4, 22, 31,'yes', 34, - 16, -16, 8 , 8] 
k = 6
str_ = "max"
print(given_nth_value(arr, k, str_), 6)
