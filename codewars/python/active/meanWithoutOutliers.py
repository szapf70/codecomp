# https://www.codewars.com/kata/5962d557be3f8bb0ca000010/train/python
# Mean without outliers

def mean(l):
    return sum(l)/len(l)

def variance(l,mean):
    lvar = 0
    for v in l:
        lvar += (v - mean)**2
    return lvar/len(l)

def stddev(v):
    return v**0.5 


def has_outliers(l,cutoff):
    lm = mean(l)
    st = stddev(variance(l,mean))
    out = [abs(lm)] 
    
def clean_mean(sample, cutoff):
    return


sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
print(clean_mean(sample,3))