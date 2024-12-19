# https://www.codewars.com/kata/59c03f175fb13337df00002e/train/python
# Make A Window

def make_a_window(num): 
    def roof(num):
        return "-" * (2*num+3)
    def mid(num):
        w = "-" * num
        return w.join(['|','+','|'])
    def win(num):
        w = "." * num
        return w.join(['|']* 3)
    
    _win = []

    _win.append(roof(num))
    for _ in range(num): _win.append(win(num))
    _win.append(mid(num))
    for _ in range(num): _win.append(win(num))
    _win.append(roof(num))
    
    return "\n".join(_win)


print(make_a_window(3))    