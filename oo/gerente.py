from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self,nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionario = qtd_funcionarios

    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso permitido')
            return True
        
        print("Acesso negado")
        return False

    def get_bonificacao(self):
        return self._salario * 0.15