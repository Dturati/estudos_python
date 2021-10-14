from abc import abstractmethod, ABC

class Sapiens(ABC):

    @abstractmethod
    def name(self):
        """name"""

    @abstractmethod
    def years(self):
        """years"""

    @abstractmethod
    def concat(self, name="", last=""):
        return name + " " + last

    def teste(self):
        print('teste')

class Human(Sapiens):

    def __init__(self, name, years):
        self.__name = name
        self.__years = years

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, years):
        self.__years = years

    def concat(self, name="", last=""):
        return super().concat(name, last)

    def __iter__(self):
        return (r for r in (self.__years, self.__name))

h = Human("", 0)
h.years = 35
h.name = "David"

# for r in h:
#     print(r)

# h.teste()
res = h.concat(h.name, "Turati")
print(res)