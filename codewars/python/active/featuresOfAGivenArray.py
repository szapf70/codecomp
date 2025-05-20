# https://www.codewars.com/kata/569ff2622f71816610000048/train/python
# Features of a Given Array

from collections import OrderedDict
class Array(object):
    def __init__(self, arr = []):
        self.arr = arr
    
    def num_elements(self):
        return len(self.arr)
    
    def num_values(self):
        return len(set(self.arr))
    
    def start_end(self):
        return [self.arr[0],self.arr[-1]]
        
    def range_(self):
        return [min(self.arr),max(self.arr)]

    def is_increasing(self,s,e):
        for i in range(s,e):
            if self.arr[i] >= self.arr[i+1]:
                return False   
        return True

    def is_decreasing(self,s,e):
        for i in range(s,e):
            if self.arr[i] <= self.arr[i+1]:
                return False   
        return True

    def largest_increas_subseq(self):
        m_len = 2
        m_slice = None
        
        for s_start in range(len(self.arr)-3):
            for s_end in range(len(self.arr)-1,s_start+1,-1):
                if self.is_increasing(s_start,s_end):
                    if len(self.arr[s_start:s_end+1]) > m_len:
                        m_len = len(self.arr[s_start:s_end+1])
                        m_slice = self.arr[s_start:s_end+1]
        if m_slice == None:
            return "No increasing subsequence"
        return m_slice

    def largest_decreas_subseq(self):
        m_len = 2
        m_slice = None
        
        for s_start in range(len(self.arr)-3):
            for s_end in range(len(self.arr)-1,s_start+1,-1):
                if self.is_decreasing(s_start,s_end):
                    if len(self.arr[s_start:s_end+1]) > m_len:
                        m_len = len(self.arr[s_start:s_end+1])
                        m_slice = self.arr[s_start:s_end+1]
        if m_slice == None:
            return "No decreasing subsequence"
        return m_slice
        
    def __str__(self):
        d = OrderedDict([('1.number of elements', self.num_elements()), 
        ('2.number of different values', self.num_values()), 
        ('3.first and last terms', self.start_end()),
        ('4.range of values', self.range_()), 
        ('5.increas subseq', self.largest_increas_subseq()), 
        ('6.decreas subseq', self.largest_decreas_subseq())])
        return str(d)


arr = [234, 230, 229, 225, 318, 317, 312, 612, 620, 613, 30, 40, 10]
c = Array(arr)
print(c)
print("Should equal --->", "OrderedDict([('1.number of elements', 13), ('2.number of different values', 13), ('3.first and last terms', [234, 10]), ('4.range of values', [10, 620]), ('5.increas subseq', [312, 612, 620]), ('6.decreas subseq', [234, 230, 229, 225])])")
