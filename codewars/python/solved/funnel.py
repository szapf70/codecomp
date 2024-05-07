# https://www.codewars.com/kata/585b373ce08bae41b800006e/train/python

class Funnel(object):
    # Coding and coding...
    data = [-1] * 15
    nodes = { 0: {"l":  1, "r":  2},
              1: {"l":  3, "r":  4},
              2: {"l":  4, "r":  5},
              3: {"l":  6, "r":  7},
              4: {"l":  7, "r":  8},
              5: {"l":  8, "r":  9},
              6: {"l": 10, "r": 11},
              7: {"l": 11, "r": 12},
              8: {"l": 12, "r": 13},
              9: {"l": 13, "r": 14},
             10: {"l": -1, "r": -1},
             11: {"l": -1, "r": -1},
             12: {"l": -1, "r": -1},
             13: {"l": -1, "r": -1},
             14: {"l": -1, "r": -1}}
    
    def gdstr(self, pos): # return datastring or whitespace if -1
        if -1 < self.data[pos] < 10:
            return str(self.data[pos])
        else:
            return " "
        
    
    def __init__(self): pass
    
    def fill(self, *args): pass
    
    def drip(self): pass
    
    def __str__(self):
        return
        


f = Funnel()
print(f.data)


"""Task
Your task is to create a Funnel data structure. It consists of three basic methods: fill(), drip() and toString()/to_s/__str__. Its maximum capacity is 15 data.

Data should be arranged in an inverted triangle, like this:

\1 2 3 4 5/
 \7 8 9 0/
  \4 5 6/
   \2 3/
    \1/
The string method should return a multi-line string to display current funnel data arrangement:

funnel = Funnel()
print(funnel)
 \         /
  \       /
   \     /
    \   /
     \ /
The method fill() should accept one or more arguments to fill in the funnel:

funnel = Funnel()
funnel.fill(1)
print (funnel)
 \         /
  \       /
   \     /
    \   /
     \1/
funnel.fill(2)
print (funnel)
 \         /
  \       /
   \     /
    \2  /
     \1/
funnel.fill(3)
print (funnel)
 \         /
  \       /
   \     /
    \2 3/
     \1/
funnel.fill(4,5)
print (funnel)
 \         /
  \       /
   \4 5  /
    \2 3/
     \1/
funnel.fill(6,7,8,9)
print(funnel)
 \         /
  \7 8 9  /
   \4 5 6/
    \2 3/
     \1/
In each row, fill() always fill data from left to right.

The method drip() should drip the bottom value out of funnel and returns this value:

(continue the example above)
v = funnel.drip()
print(v)
1
print(funnel)
 \         /
  \  8 9  /
   \7 5 6/
    \4 3/
     \2/
As you can see, the bottom 1 was dripping out. The number above it will fill it's place. The rules to 
fill are: Select one of the two numbers above it, which bear the "weight" of relatively large. In other 
words, there are more numbers on this number. Is this a bit hard to understand? Please see the following:

 In the example above, before the execution of drip(), funnel is:
  \         /
   \7 8 9  /
    \4 5 6/
     \2 3/
      \1/
After drip(), 1 will be dripped out.
We should choose a number between 2 and 3 to fill the place of 1.
2 has 5 numbers on it(4,5,7,8,9). 3 has 4 numbers on it(5,6,8,9)
So we choose 2 to fill the place of 1
And now, the place of 2 is empty.
We also need choose a number between 4 and 5 to fill the place of 2.
4 has 2 numbers on it(7,8). 5 has 2 numbers on it too(8,9)
There are same "weight" on 4 and 5,
In this case, we choose the number on the left
So we choose 4 to fill the place of 2
And then choose 7 to fill the place of 4
Let us continue to drip():

funnel.drip()
print(funnel)
 \         /
  \    9  /
   \7 8 6/
    \5 3/
     \4/

funnel.drip()
print(funnel)
 \         /
  \       /
   \7 9 6/
    \8 3/
     \5/

funnel.drip()
print(funnel)
 \         /
  \       /
   \  9 6/
    \7 3/
     \8/

funnel.drip()
print(funnel)
 \         /
  \       /
   \    6/
    \7 9/
     \3/

funnel.drip()
print(funnel)
 \         /
  \       /
   \     /
    \7 6/
     \9/

funnel.drip()
print(funnel)
 \         /
  \       /
   \     /
    \  6/
     \7/

funnel.drip()
print(funnel)
 \         /
  \       /
   \     /
    \   /
     \6/

funnel.drip()
print(funnel)
 \         /
  \       /
   \     /
    \   /
     \ /
When the funnel is empty, drip() will return null/nil/None

Another edge case is: When funnel is full, fill() will not change the funnel.

A bit complex..."""
