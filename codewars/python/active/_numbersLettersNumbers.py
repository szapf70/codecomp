# https://www.codewars.com/kata/599febdc3f64cd21d8000117/train/python
# Numbers of Letters of Numbers


def tr(p):
    t = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    res = ""
    for d in str(p):
        res += t[int(d)]
    return res

def numbers_of_letters(n):
    
    res = []
    while res == [] or res[-1] != 'four':
        if res == []:
            res.append(tr(n))
        else:
            res.append(tr(len(res[-1])))
    return res    






print(numbers_of_letters(1), ["one", "three", "five", "four"])
print(numbers_of_letters(12), ["onetwo", "six", "three", "five", "four"])
print(numbers_of_letters(37), ["threeseven", "onezero", "seven", "five", "four"])
print(numbers_of_letters(311), ['threeoneone', 'oneone', 'six', 'three', 'five', 'four'])
print(numbers_of_letters(999), ["nineninenine", "onetwo", "six", "three", "five", "four"])
