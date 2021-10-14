import abc
from abc import ABC

class Tombola(ABC):
    
    @abc.abstractmethod
    def load(self, iterable):
        """Adiciona"""
        return iterable + 1

    @abc.abstractmethod
    def pick(self):
        """Remove"""
        print("pick")

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
