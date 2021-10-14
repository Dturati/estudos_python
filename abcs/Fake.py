from Tombola import Tombola

class Fake(Tombola):
    def pick(self):
        return 13

    def load(self, iterable):
        """"Todo"""

    @classmethod
    def teste_local(cls):
        print('teste_local')


f = Fake()
Fake.teste_local()