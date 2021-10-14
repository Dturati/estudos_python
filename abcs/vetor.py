class V2d:
    typecode = ''

    def __init__(self, x=1, y=1) -> None:
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

class V2d2:
    typecode = ''

    def __init__(self, x=1, y=1) -> None:
        self.__x = float(x)
        self.__y = float(y)


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        self.__x = float(x)
    
    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

v = V2d2(1,2)
v.x = 10
for r in v:
    print(r)