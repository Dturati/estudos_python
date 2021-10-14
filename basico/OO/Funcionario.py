class Funcionario:
    _salario = 0

    def __init__(self,salario):
        self._salario = salario

    def bonifica(self, valor):
        self._salario += valor

    def get_salario(self):
        return self._salario
     
