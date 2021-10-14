class Porto:
    def __init__(self, nome=''):
        self.nome = nome

    def executa(self):
        print('Desenvolvedor...')

class Funcionario(Porto):
    def executa(self):
        print('Executa funcionario...')

class Gerente(Porto):
    def executa(self):
        print('Executa Gerente...')


class Mixins:
    def __str__(self):
        return f'Mixins, {self.nome}'

class Junior(Funcionario):
    pass

class Pleno(Funcionario, Gerente,Mixins):
    pass


junior = Junior()
junior.executa()

pleno = Pleno('David')
pleno.executa()
print(pleno)