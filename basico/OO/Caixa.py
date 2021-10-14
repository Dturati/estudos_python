from Funcionario import Funcionario

class Caixa(Funcionario):

    def __init__(self,salario=0):
        super().__init__(salario)
