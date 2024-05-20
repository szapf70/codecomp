# https://www.codewars.com/kata/58311536e77f7d08de000085/train/python
# How many cows do you have?

def count_cows(n):
    adult_cows = 0
    gcows = [1,0,0]
    for y in range(1,n+1):
        adult_cows += gcows.pop()
        gcows.insert(0,adult_cows)
    return sum(gcows)+adult_cows

print(count_cows(10))


"""
Consider having a cow that gives a child every year from her fourth year of life on and all her subsequent children do the same.

After n years how many cows will you have?

After n years	Cow count
0	1
1	1
3	2
4	3
10	28
Return null if n is not an integer.

Note: Assume all the cows are alive after n years.




"""


