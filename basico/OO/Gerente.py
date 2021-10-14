from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, valor=0):
        super().__init__(valor)
