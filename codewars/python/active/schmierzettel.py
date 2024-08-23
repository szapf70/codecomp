print("Test \u25A0 \u25A1 Test")

n = 10
le = " ".join(["\u25A0" if i%2 else "\u25A1" for i in range(n)])
lo = " ".join(["\u25A1" if i%2 else "\u25A0" for i in range(n)])
if n%2:
    le, lo = lo, le
print("\n".join([le if not i%2 else lo for i in range(n)])) 