class Init:

    _total = 0

    def __init__(self, value):
        type(self)._total += value

    @classmethod
    def get_total(cls):
        return cls._total
    
    def get_normal(self):
        return self._total


c1 = Init(100)
print(c1.get_total())
c2 = Init(200)

print(c2.get_total())