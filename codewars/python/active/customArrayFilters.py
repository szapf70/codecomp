# https://www.codewars.com/kata/53fc954904a45eda6b00097f/train/python
# Custom Array Filters

class list(list):
    def __init__(self, *args):
        super().__init__(args)

    def even(self):
        return [i for i in self[0] if not i%2]
    
    def odd(self):
        return [i for i in self[0] if i%2]
    
    def under(self,n):
        return [i for i in self[0] if i < n]
    
    def over(self,n):
        return [i for i in self[0] if i > n]
    
    def in_range(self,m,n):
        return [i for i in self[0] if m <= i <= n]

print(list([1,2,3,4,5]).even(), [2,4])
print(list([1,2,3,4,5]).odd(), [1,3,5])    