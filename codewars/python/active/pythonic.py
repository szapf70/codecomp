
# Kein "Pythonic code"
f = open('file.txt')
a = f.read()
print(a)
f.close()


# "Pythonic code"
with open('file.txt') as f:
    for line in f:
        print(line)
        
        


