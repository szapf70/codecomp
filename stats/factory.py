class Datei:
    def __new__(cls, size, *args, **kwargs):
        if cls is Datei:
            if size <= 20000:
                return super(Datei, File).__new__(File)
            elif size > 20000:
                return super(Datei, Cache).__new__(Cache)
            else:
                raise ValueError("Ungültige Größe")
        return super(Datei, cls).__new__(cls, *args, **kwargs)

class File(Datei):
    def display(self):
        print("Speicherlösung")

class Cache(Datei):
    def display(self):
        print("Cachelösung")
        

d1 = Datei(5000)
print(d1)
d2 = Datei(100000)
print(d2)