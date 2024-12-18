# https://www.codewars.com/kata/5a0117798ba9143a64000073/train/python
# @htmlize


def htmlize(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            org_res = func(*args, **kwargs)     
            return f"<{tag}>{org_res}</{tag}>"
        return wrapper
    return decorator
    
    
@htmlize('html')
@htmlize('test')
def gen_str(s):
    return s[::-1]



print(gen_str('Blabla'))
