
"""
Vamos fazer um  jogo rápido aqui, vamos falar rapidinho aqui sobre closures em python
Uma closure em python (ou em qualquer linguagem), é quando funções aninhadas acessam variáveis de uma função externa, quando as funções são aninhadas, a função pode acessar variáveis não globais
definidas fora do seu escopo
"""

# Exemplo 1
"""
Aqui temos uma observação importante, a variável lista é um objeto mutável, ou seja, voce pode alterar o estado do objeto com o append
"""
def lancar_notas1():

  lista_notas = []

  def processar(nova_nota):
    lista_notas.append(nova_nota)
    qtd_notas = len(lista_notas)
    media = sum(lista_notas) / qtd_notas
    res = {
      "media": media,
      "qtd_notas": qtd_notas
    }
    return res
  
  return processar

fn1 = lancar_notas1()
print(fn1(5))
print(fn1(10))

#exemplo 2

"""
 Nesse exemplo em vez de usar um objeto mutável, vamos usar variáveis do tudo int, que são imutávis e ver o que acontece
"""
def lancar_notas2():

  total = 0
  qtd_notas = 0

  def processar(nova_nota):
    nonlocal total, qtd_notas
    qtd_notas += 1
    total += nova_nota
    media = total / qtd_notas
    
    res = {
      "media": media,
      "total": total
    }

    return res
  return processar

"""
Ao executar a função fn2, ocorre um erro, 'UnboundLocalError: local variable 'qtd_notas' referenced before assignment',
isso ocorre por que a atribuição em 'qtd_notas e total, redeclara a variável no escopo local da função 'processar' e as
variáveis deixam de ser livres, Strings, inteiros e tuplas são imutáveis em python, as tornando variáveis locais, antes do python 3 não existia uma tratativa direta para isso, era comum
usar variáveis imutaveis dentro de um objeto mutável, usando um dict por exemplo.
"""

fn2 = lancar_notas2()
print(fn2(5))
print(fn2(10))

