from abc import ABC

class Programa:
    my_name = "David"

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0
    
    def dar_like(self):
        self._likes += 1
    
    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @classmethod
    def teste(cls):
        print(f'Nome: {cls.my_name}')

    def __str__(self):
        return f'{self._nome} | {self._likes} | {self._ano}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome=nome, ano=ano)
        self._duracao = duracao

    
    def __str__(self):
        return f'{self._nome} | {self._likes} | {self._ano} | {self._duracao} min'
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome=nome, ano=ano)
        self._temporadas = temporadas

    def __str__(self):
        return f'{self._nome} | {self._likes} | {self._ano} | {self._temporadas} temp'

class PlayList:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas
    
    def tam(self):
        return len(self._programas)

    def __getitem__(self, pos):
        return self._programas[pos]
    
    def __len__(self):
        return len(self._programas)


retur_to_home = Filme("return to home",2018, 140)
retur_to_home.nome = "return to home"
retur_to_home.dar_like()

breaking_bad = Serie("breaking_bad", 2018,7)
breaking_bad.dar_like()

filmes_series = [breaking_bad, retur_to_home]

play_list = PlayList("Ver", filmes_series)
print(len(play_list))
for el in play_list:
    print(el)

print(f'Está: {breaking_bad in play_list}')