from Autenticavel import Autenticavel

class Gerente(Autenticavel):
    def autentica(self, senha=123):
        print("Autentica Gerente")