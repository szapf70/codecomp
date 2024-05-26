# https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/train/python
# k-Primes

pt = [2]

def fillPrimeTable(n):
    for n in range(pt[-1]+1,n+1):
        isPrime = True
        lidx = 0
        thres = int(n**0.5)
        while pt[lidx] <= thres:
            if n%pt[lidx] == 0:
                isPrime = False
            lidx += 1
        if isPrime:
            pt.append(n)        

def prime_factors(n):
    ns = n
    nt = int(n**0.5)+1
    fillPrimeTable(nt)
    fac = []
    pidx = 0
    while n > 1 and pidx < len(pt) and pt[pidx] <= nt :
        if ns%pt[pidx] == 0:
            fac.append(pt[pidx])
            ns = ns // pt[pidx]
        else:
            pidx += 1
    if ns == n:
        fac.append(n)
    
    return len(fac)

def count_Kprimes(k, start, nd):
    res = []
    for n in range(start, nd+1):
        if prime_factors(n) == k:
            res.append(n)
    return res

def puzzle(s):
    pass
    # your code 

print(count_Kprimes(5,500,600))

"""
A natural number is called k-prime if it has exactly k prime factors, counted with multiplicity. For example:

k = 2  -->  4, 6, 9, 10, 14, 15, 21, 22, ...
k = 3  -->  8, 12, 18, 20, 27, 28, 30, ...
k = 5  -->  32, 48, 72, 80, 108, 112, ...
A natural number is thus prime if and only if it is 1-prime.

Task:
Complete the function count_Kprimes (or countKprimes, count-K-primes, kPrimes) which is given parameters k, start, end (or nd) and returns an array (or a list or a string depending on the language - see "Solution" and "Sample Tests") of the k-primes between start (inclusive) and end (inclusive).

Example:
countKprimes(5, 500, 600) --> [500, 520, 552, 567, 588, 592, 594]
Notes:

The first function would have been better named: findKprimes or kPrimes :-)
In C some helper functions are given (see declarations in 'Solution').
For Go: nil slice is expected when there are no k-primes between start and end.
Second Task: puzzle (not for Shell)
Given a positive integer s, find the total number of solutions of the equation a + b + c = s, where a is 1-prime, b is 3-prime, and c is 7-prime.

Call this function puzzle(s).

Examples:
puzzle(138)  -->  1  because [2 + 8 + 128] is the only solution
puzzle(143)  -->  2  because [3 + 12 + 128] and [7 + 8 + 128] are the solutions
NUMBER THEORYMATHEMATICSALGORITHMS
"""    