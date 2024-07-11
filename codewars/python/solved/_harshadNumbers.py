# https://www.codewars.com/kata/54a0689443ab7271a90000c6/train/python
# Harshad or Niven numbers

class Harshad:

    @staticmethod
    def digit_sum(number):
        return sum([int(d) for d in str(number)])

    @staticmethod
    def is_valid(number):
        return not number%Harshad.digit_sum(number)
        
    @staticmethod
    def get_next(number):
        n = n + 1
        while not Harshad.is_valid(n):
            n += 1
        return n            
    
    @staticmethod
    def get_series(count, start=0):
        res = []
        
        for _ in range(count):
            if res == []:
                res.append(Harshad.next(start))
            else:
                res.append(Harshad.next(res[-1]))    
        return res