"""
Farmer John needs to build a new fence. He has marked the starting and ending points of the fence line. To ensure the fence
is sturdy, he wants to place (n) posts at equal intervals along the line between the start and the endpost. John needs a program to calculate the exact positions where he should
dig the holes for the posts. Can you help him by writing a function that takes the start and end points of the line and the number of posts 
and returns their positions?

"""
from random import uniform,randint

def calc_post_positions(start, end, n):
    if n < 0 or start == end:
        return "Fence could not be build!"
    
    x1, y1 = start
    x2, y2 = end

    x_ival = (x2 - x1) / (n + 1)
    y_ival = (y2 - y1) / (n + 1)

    posts = [(round(x1 + i * x_ival,2), round(y1 + i * y_ival,2)) for i in range(1, n + 1)]
    
    posts.insert(0, start)
    posts.append(end)
    
    return posts


def genTests():
    with open('farmerJohnsFenceTests.py', "w") as t:
        for _ in range(50):    
            s = (round(uniform(-25.0, 25.0),2),round(uniform(-25.0, 25.0),2))
            e = (round(uniform(-25.0, 25.0),2),round(uniform(-25.0, 25.0),2))
            n = randint(0,10)
            prel1 = "        test.assert_equals(calc_post_positions("
            l1 = f"{s}, {e}, {n}),\n"
            l2 =   f"        {calc_post_positions(s,e,n)})\n"
            t.write(prel1+l1)
            t.write(l2)
        
        
    
"""

# Example usage
start = (-15.0, -15.0)
end = (15.0, 15.0)
num_posts = 5

post_positions = calc_post_positions(start, end, num_posts)
print(post_positions)

"""

genTests()