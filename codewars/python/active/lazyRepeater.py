# https://www.codewars.com/kata/51fc3beb41ecc97ee20000c3/train/python
# Lazy Repeater





# define two methods 
 
# second method that will be returned
# by first method
     
# first method that return second method
def A(str):
    def B():
        lstr = str
        print(str)
        lstr = lstr[-1]+lstr[:j-1]

    print("Inside the method A.")
     
    # return second method
    return B
 
# form a object of first method 
# i.e; second method
returned_function = A("Test")
 
# call second method by first method
returned_function()
returned_function()