# https://www.codewars.com/kata/56d082c24f60457198000e77/train/python
# Get the Excel column title!

def get_column_title(num):
    col = ""
    while True:
        if num > 26:
            num, mi = divmod(num-1,26)
            col = chr(mi+ord('A')) + col
        else:
            return chr(num+ord('A')-1) + col    
    
print(get_column_title(52))
"""
test.assert_equals(get_column_title(26), "Z")
test.assert_equals(get_column_title(52), "AZ")
test.assert_equals(get_column_title(53), "BA")
test.assert_equals(get_column_title(702), "ZZ")

"""