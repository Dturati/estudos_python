from random import shuffle
class Pessoa:

    def __init__(self, pessoas: list) -> None:
        self.__pessoas  = pessoas

    @property
    def pessoas(self):
        return self.__pessoas
    
    @pessoas.setter
    def pessoas(self, pessoas: list):
        return self.__pessoas

    def __getitem__(self, x):
        return self.__pessoas[x]

    def __iter__(self):
        return (r for r in self.__pessoas)

    def __len__(self):
        return len(self.__pessoas)

    def __setitem__(self,position, pessoas):
        self.__pessoas[position] = pessoas

nomes = ["Liliane", "Adrea", "marielle", "Ana Paula", "Gleice"]

p = Pessoa(nomes)
shuffle(p)
for r in p:
    print(r)



print(f"Que delicia, {p[0]}, quer leitinho?")