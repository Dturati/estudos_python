from funcionario.Diretor import Diretor
# from funcionario.Gerente import Gerente

class SistemaInterno:
    def login(self, funcionario):
        funcionario.autentica()


sistema = SistemaInterno()
# gerente = Gerente()
diretor = Diretor(1234)

sistema.login(diretor)

