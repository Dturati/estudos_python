class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + self._salario * 0.05


class Controle:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes
    
    def registra(self, funcionario):
        self._total_bonificacoes = funcionario.get_bonificacao()
    
    # @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

funcionario = Funcionario("Jose",'017.534.911-86',4000)
gerente = Gerente("David",'017.534.911-85',4000,123,10)

controle = Controle()

controle.registra(gerente)
print(controle.total_bonificacoes())
controle.registra(funcionario)
print(controle.total_bonificacoes())
