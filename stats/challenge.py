import time
import szstat
import szstatpro
import random
import gc

# Liste aller Durchläufe

results = []

# Einheitlicher Seed für alle Benchmarks
random.seed(1337)
# Erzeugt Basisdatensatz für den Benchmark
bdata = []
for _ in range(35000):
    bdata.append(random.randint(0,1000))

# Benchmark  szstat
sz1 = szstat.SZStat(bdata[:20000])
sz_start = time.time()
for v in bdata[20000:]:
    sz1.data.append(v)
    _ = sz1.getRange()
    _ = sz1.getMean()
    
szr = sz1.Desc()
szr['time'] = time.time() - sz_start
szr['name'] = "SZStat"

# Benchmark  szstatpro
gc.disable()
sz2 = szstatpro.SZStatPro(bdata[:20000])
szp_start = time.time()
for v in bdata[20000:]:
    sz2.addValue(v)
    _ = sz2.getRange()
    _ = sz2.getMean()
    
szpr = sz2.Desc()
szpr['time'] = time.time() - szp_start
szpr['name'] = "SZStatPro"
szpr['speedf'] = szr['time'] / szpr['time']
results.append(szpr)


gc.enable()

for r in results:
    l = f"{r['name']:>10} - {r['speedf']:.2f} times faster."
    for k in ['median','mean','variance','stddev']:
        if szr[k] != r[k]:
            l += " But result are wrong."
    print(l)        







