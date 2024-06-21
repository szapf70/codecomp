import time
import szstat
import random


# Einheitlicher Seed für alle Benchmarks

random.seed(1337)

# Erzeugt Basisdatensatz für den Benchmark
bdata = []
for _ in range(10000):
    bdata.append(random.randint(0,1000))


print(bdata)

# Benchmark - 

#sz1 = szstat.SZStat(bdata)

#print(sz1.Desc())
#print(sz1.Report())








