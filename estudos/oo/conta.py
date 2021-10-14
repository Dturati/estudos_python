class Conta:
    def __init__(self, numero=0, titular="" ,saldo=0, limite=0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite =  limite
        self._codigo_banco = "001"

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if (valor <= (self._saldo + self._limite)):
            self._saldo -= valor
        else:
            print("Limite insuficiênte {}".format(self._limite))
        
    def extrato(self):
        print("O saldo é: {}, Titular: {}".format(self._saldo, self._titular))

    def get_saldo(self):
        self._saldo
    
    def get_titular(self):
        return self._titular

    def transfere(self, conta, valor: float):
        conta.deposita(valor)
        self.saca(valor)

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, value):
        self._limite = value

    @staticmethod
    def codigo_banco():
        return "001"

conta1 = Conta(1,"David Turati",100,100)
# conta1.deposita(10)
# conta2 = Conta(2,"José Turati",45000,45000)
# conta1.transfere(conta2,1000)
# conta.saca(100)
conta1.extrato()
# conta2.extrato()
conta1.limite = 10
print(conta1.limite)

conta1.saca(120)

print(conta1.codigo_banco())