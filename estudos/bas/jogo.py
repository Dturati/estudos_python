import random
import teste as ts

nome = "David"
sobre = "Turati"
print("Meu nome: {1} {0}".format(nome, sobre))

num = 34.4342342423

print("Numero:{:010.3f}".format(num))

teste = f"meu nome é: {nome}"

print(teste)

print(random.randrange(1,4))

if __name__ == "__main__":
    # print('teste')
    ts.my_teste()