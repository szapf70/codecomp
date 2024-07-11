# https://www.codewars.com/kata/581331293788bc1702001fa6/train/python
# Framed Reflection

def mirror(text):
    t = text.split()
    l = max([len(w) for w in t])
    for i in range(len(t)):
        t[i] = "* " + t[i][::-1].ljust(l) + " *"
    f = "*" * (l+4)
    t.insert(0,f)
    t.append(f)
    return "\n".join(t)
    
        
print(mirror("Hello World"))    
print(mirror("Codewars"))    
    
    
