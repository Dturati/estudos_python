class Conta:
    _total_contas = 0
    _idade = 0

    __slots__ = ['_total_contas','_idade']

    def __init__(self, num):
        self._total_contas += 1

    @classmethod
    def get_tatal_contas(cls):
        return cls._total_contas
    
    @staticmethod
    def total_contas():
        return 0

conta = Conta(100)
print(conta.get_tatal_contas())
print(Conta.get_tatal_contas())
print(Conta.total_contas())

# conta.idade = 34

# print(conta.idade)
