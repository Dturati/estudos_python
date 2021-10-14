@property
def foo(self):
    _foo = 100
    return self._foo


foo.setter(200)

print(foo._foo)