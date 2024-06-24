import time
import szstat
import random
import gc

# Einheitlicher Seed für alle Benchmarks

random.seed(1337)

# Erzeugt Basisdatensatz für den Benchmark
bdata = []
for _ in range(20000):
    bdata.append(random.randint(0,1000))

# Benchmark  

sz1 = szstat.SZStat(bdata)
print(sz1.Report())

sz_start = time.time()
for _ in range(15000):
    sz1.data.append(random.randint(0,1000))
    _ = sz1.getMean()
    
sz_end = time.time()

print(sz1.Report())

print(f"Durchlauf mit Durchschnittsberechung {sz_end - sz_start:.5f} Sekunden")

    







