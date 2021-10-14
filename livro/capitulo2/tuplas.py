tuple = ('David','Turati')

nome, sobrenome = tuple

print(nome,sobrenome)

def teste(nome, sobrenome):
    print(nome, sobrenome)

teste(*tuple)

a,b,*rest = range(5)

print(a,b,rest)