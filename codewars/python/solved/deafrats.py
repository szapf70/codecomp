# https://www.codewars.com/kata/598106cb34e205e074000031/train/python
# The Deaf Rats of Hamelin

def count_deaf_rats(town):
    lrats = (town[:town.index('P')]  + town[town.index('P')+1:][::-1]).replace(' ', '')
    drats = 0
    for i in range(0,len(lrats),2):
        if lrats[i] == 'O': drats += 1 
    return drats
    
    
    # Your code here
    pass


print(count_deaf_rats("~O~O~O~OP~O~OO~"))
"""
@test.it("ex1")
def ex1():
    test.assert_equals(count_deaf_rats("~O~O~O~O P"), 0)
  
@test.it("ex2")
def ex2():
    test.assert_equals(count_deaf_rats("P O~ O~ ~O O~"), 1)
  
@test.it("ex3")
def ex3():
    test.assert_equals(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)
"""