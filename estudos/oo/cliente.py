class Cliente:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome.title()



cliente = Cliente("david")
print(cliente.nome)