# https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611/train/python
# Length of missing array

def get_length_of_missing_array(array_of_arrays):
    lgths = [len(a) for a in array_of_arrays]
    maxl = max(lgths)
    
    return int((maxl * (maxl +1)/2) - sum(lgths))


print(get_length_of_missing_array([['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], ['a', 'a', 'a', 'a','a', 'a']]))