# https://www.codewars.com/kata/5264603df227072e6500006d/train/python
# The Fruit Juice

class Jar():
    def __init__(self):
        self.jcs = {}
    
    def add (self, amount, kind):
        self.jcs[kind] = self.jcs.get(kind, 0) + amount
    
    def pour_out (self, amount):
        if amount >= self.get_total_amount():
            self.jcs = {}
        por = self.get_total_amount() / amount
        for j in jcs:
            self.jcs[j] -= self.jcs[j]*por

    def get_total_amount(self):
        ta = 0
        for j in jcs.keys():
            ta += self.jcs[j]
        return ta    
    
    def get_concentration(self, kind):
        if kind in self.jcs:
            return self.get_total_amount() / self.jcs[kind]