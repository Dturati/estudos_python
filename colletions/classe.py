class ContaCorrente:
    
    def __init__(self, codigo) -> None:
      self.codigo = codigo
      self.saldo = 0

    
    def deposita(self, valor):
      self.saldo += valor
      return self

    def __str__(self) -> str:
        return "[Codigo {} saldo {}]".format(self.codigo, self.saldo)


conta = ContaCorrente(10)\
                      .deposita(1000)

print(conta)