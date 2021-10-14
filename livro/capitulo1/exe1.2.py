from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __boo__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2,4)
v2 = Vector(1,1)
v3 = v1 + v2
v4 = v1 * 2
print(v3)
print(v4)