from gerente import Gerente
from vendedor import Vendedor
from controle import ControleBonificacao
from funcionario import Funcionario

gerente = Gerente("David","017-534-911-85",5000.0000,"123",1)
vendedor = Vendedor("jao","017-534-911-85",5000.0000)
controle =  ControleBonificacao()

print(gerente.get_bonificacao())
print(vendedor.get_bonificacao())

controle.registra(vendedor)
controle.registra(gerente)

print(controle.total_bonificacao)