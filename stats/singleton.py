class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Wird einmalig erzeugt.')
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
 
 
 
p1 = Point(10,20)    
p1.x = 25


p2 = Point(20,20)
print(p1)
print(p2)


l1 = Logger()
l2 = Logger()    
print(l1)
print(l2)    