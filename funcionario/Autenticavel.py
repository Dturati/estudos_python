from funcionario.Funcionario import Funcionario

class Autenticavel(Funcionario):
    def autentica(self,senha=123):
        super().autentica(senha)