# https://www.codewars.com/kata/5ae840b8783bb4ef79000094/train/python
# Dictionary Merge

def merge(*dicts):
    res = {}
    for dict in dicts:
        if dict == {}:
            continue
        for k,v in dict.items():
            if not k in res:
                res[k] = [v]
            else:
                res[k].append(v)
    
    return res

source1 = {"A": 1, "B": 2} 
source2 = {"A": 3}

print(merge(source1, source2))
# result should have this content: {"A": [1, 3]}, "B": [2]}

