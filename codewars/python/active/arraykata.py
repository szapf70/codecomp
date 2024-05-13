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
        
    def largest_increas_subseq(self):
        top = {"l" : 0, "s" : 0, "e" : 0}
        act = {"l" : 0, "s" : 0, "e" : 0}
        run = False

        i = 2
        while i <= len(self.arr):
            if i == len(self.arr):
                if run:
                    if act['l'] > top['l']:
                        top = act
                break
            if self.arr[i-2] < self.arr[i-1] < self.arr[i]:
                if run:
                    act['l'] += 1
                else:
                    act['l'] = 3
                    act['s'] = i -2
                    run = True
            else:
                if run:
                    act['e'] = i - 1
                    run = False
                    if act['l'] > top['l']:
                        top = act  
                        act = {'l' : 0, 's' : 0,'e' :0}     

            i += 1
        if top['l'] == 0:
            return "No increasing subsequence"
        return self.arr[top['s']:top['e']+1]


    def largest_decreas_subseq(self):
        top = {"l" : 0, "s" : 0, "e" : 0}
        act = {"l" : 0, "s" : 0, "e" : 0}
        run = False

        i = 2
        while i <= len(self.arr):
            print(self.arr[act['s']:act['e']+1],run)
            if i == len(self.arr):
                if run:
                    if act['l'] > top['l']:
                        top = act
                break        
            if self.arr[i-2] > self.arr[i-1] > self.arr[i]:
                if run:
                    act['l'] += 1
                else:
                    act['l'] = 3
                    act['s'] = i -2
                    run = True
            else:
                if run:
                    act['e'] = i - 1
                    run = False
                    if act['l'] > top['l']:
                        top = act  
                        act = {'l' : 0, 's' : 0,'e' :0}     

            i += 1

        if top['l'] == 0:
            return "No decreasing subsequence"
        return self.arr[top['s']:top['e']+1]
        
    def __str__(self):
        d = OrderedDict([('1.number of elements', self.num_elements()), 
        ('2.number of different values', self.num_values()), 
        ('3.first and last terms', self.start_end()),
        ('4.range of values', self.range_()), 
        ('5.increas subseq', self.largest_increas_subseq()), 
        ('6.decreas subseq', self.largest_decreas_subseq())])
        return str(d)

arr = [224, 142, 429, 487, 362, 286, 767, 773, 717, 636, 70, 567, 789, 764, 537, 1203, 167, 695, 366, 788, 987, 829, 713, 188, 143, 396, 1159, 1146, 1133, 729, 417, 868, 33, 582, 684, 729, 916, 412, 700, 753, 85, 1020, 874, 1121, 522, 1222, 1142, 1123, 1084, 976, 944, 876, 789, 677, 631, 561]    
#arr = [345, 288, 250, 215,187, 156, 32, 32, 45, 12, 45, 47, 49, 55, 90, 104, 20, 30, 34]
c = Array(arr)
print(c)

"""
"OrderedDict([('1.number of elements', 56), 
('2.number of different values', 54), 
('3.first and last terms', [224, 561]), 
('4.range of values', [33, 1222]), 
('5.increas subseq', [33, 582, 684, 729, 916]), 
('6.decreas subseq', [987, 829, 713, 188, 143])])" should equal 

"OrderedDict([('1.number of elements', 56), 
('2.number of different values', 54), 
('3.first and last terms', [224, 561]), 
('4.range of values', [33, 1222]), 
('5.increas subseq', [33, 582, 684, 729, 916]), 
('6.decreas subseq', [1222, 1142, 1123, 1084, 976, 944, 876, 789, 677, 631, 561])])"



arr = [345, 32, 45, 12, 45, 47, 49, 55, 90, 104, 20, 30, 34]
c = Array(arr)
c.num_elements() == 13
c.num_values() == 12
c.start_end() == [345, 34]
c.range_() == [12, 345]
c.largest_increas_subseq() == [12, 45, 47, 49, 55, 90, 104]
c.largest_decreas_subseq() == "No decreasing subsequence" # [345, 32], [45,12] length less than 3
c.__str__() == OrderedDict([('1.number of elements', 13), ('2.number of different values', 12), ('3.first and last terms', [345, 34]), ('4.range of values', [12, 345]), ('5.increas subseq', [12, 45, 47, 49, 55, 90, 104]), ('6.decreas subseq', 'No decreasing subsequence')])

('5.increas subseq', [12, 45, 47, 49, 55, 90, 104]), ('6.decreas subseq', [345, 288, 250, 215, 187, 156, 32])])

"""