import timeit
from random import randint
from collections import deque

class beginner():
    def __init__(self, limit=3, data=[]):
        self.data = data[-limit:]
        self.limit = limit

    def mean(self):
        if len(self.data) > self.limit:
            self.data = self.data[-self.limit:]
        self.data = list(filter(lambda vt: type(vt) == int, self.data))    
        return sum(self.data) / len(self.data)
    
class intermediate():    
    def __init__(self, limit=3, data=[]):
        self._data = data[-limit:]
        self._limit = limit
        self._sum = sum(self._data)
        self._len = len(self._data)

    def push(self, value):
        if type(value) == int:
            self._data.append(value)
            self._sum += value
            if self._len == self._limit:
                self._sum -= self._data.pop(0)
            else:
                self._len += 1    

    def mean(self):
        return self._sum / self._len

class professionel():
    def __init__(self, limit=3, data=[]):
        self._data = deque(data[-limit:])
        self._limit = limit
        self._sum = sum(self._data)
        self._len = len(self._data)

    def push(self, value):
        if type(value) == int:
            self._data.append(value)
            self._sum += value
            if self._len == self._limit:
                self._sum -= self._data.popleft()
            else:
                self._len += 1    

    def mean(self):
        return self._sum / self._len


def beginner_init(limit): 
    data = [randint(0,1000) for _ in range(limit)]
    b = beginner(limit, data)
    return b

def beginner_mean(vol,limit):
    b = beginner_init(limit)
    for _ in range(vol):
        b.data.append(randint(0,1000))
        _ = b.mean()

def intermediate_init(limit): 
    data = [randint(0,1000) for _ in range(limit)]
    b = intermediate(limit, data)
    return b

def intermediate_mean(vol,limit):
    b = intermediate_init(limit)
    for _ in range(vol):
        b.push(randint(0,1000))
        _ = b.mean()

def professionel_init(limit): 
    data = [randint(0,1000) for _ in range(limit)]
    b = professionel(limit, data)
    return b

def professionel_mean(vol,limit):
    b = professionel_init(limit)
    for _ in range(vol):
        b.push(randint(0,1000))
        _ = b.mean()

In = 100   
Mn = 1     

bI = timeit.timeit("beginner_init(10000)", globals=globals(),number=In)
bM = timeit.timeit("beginner_mean(2500,10000)", globals=globals(),number=Mn)

iI = timeit.timeit("intermediate_init(10000)", globals=globals(),number=In)
iM = timeit.timeit("intermediate_mean(2500,10000)", globals=globals(),number=Mn)

pI = timeit.timeit("professionel_init(10000)", globals=globals(),number=In)
pM = timeit.timeit("professionel_mean(2500,10000)", globals=globals(),number=Mn)

print(f"Timeit - Report")
print(f"{In} * init in (s)")
print(f"beginner {bI:.2f} secs")
print(f"intermediate {iI:.2f} secs - {bI/iI:.2f} times faster.")
print(f"professionel {pI:.2f} secs - {bI/pI:.2f} times faster.")

print(f"{Mn} * mean in (s)")
print(f"beginner {bM:.2f} secs")
print(f"intermediate {iM:.2f} secs - {bM/iM:.2f} times faster.")
print(f"professionel {pM:.2f} secs - {bM/pM:.2f} times faster.")

