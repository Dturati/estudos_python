#exemplo em OO
class LancarNotas:

  def __init__(self) -> None:
      self.notas = []
  
  def __call__(self, nota):
    self.notas.append(nota)
    media = sum(self.notas) / len(self.notas)
    return media

obj = LancarNotas()
print(f"média: {obj(5)}")
print(f"média: {obj(10)}")

print('--------------')


"""
Listas são tipos mutáveis
notas é uma variável livre e mutável
"""
def lancar_notas():
  notas = []

  def fazer(nota):
    notas.append(nota)
    media = sum(notas) / len(notas)
    return media
  return fazer

notas = lancar_notas()
print(f"média: {notas(5)}")
print(f"média: {notas(10)}")
print('----------------')

"""
Números, strings e tuplas são imutáveis
"""
def lancar_notas2():
  qtd_notas = 0
  notas = 0

  def fazer(value):
   nonlocal qtd_notas, notas
   qtd_notas += 1
   notas += value
   medias =  notas / qtd_notas
   return medias

  return fazer

notas2 = lancar_notas2()
print(f"média: {notas2(5)}")
print(f"média: {notas2(10)}")
print('----------------')


