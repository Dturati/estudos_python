from funcionario.Autenticavel import Autenticavel

class Diretor(Autenticavel):
    def __init__(self, senha=123):
        self._senha = senha

    def autentica(self):
        super().autentica(self._senha)