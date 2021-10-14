from Gerente import Gerente
from Caixa import Caixa
from Bonifica import Bonifica

gerente1 = Gerente(10000)
print(gerente1.get_salario())

caixa1 = Caixa(2000)
print(caixa1.get_salario())

bonificador = Bonifica()
bonificador.set_bonus(gerente1,1000)
bonificador.set_bonus(caixa1, 500)

print("Depois do bonus")
print(gerente1.get_salario())
print(caixa1.get_salario())