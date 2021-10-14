notas_alunos = {
    'João': [0, 5, 10],
    'Clara': [7, 9, 8],
    'Maciel': "",
    'Jonas': [0, 1],
    'Maria': [5, 7, 10],
    'Marcelo': [],
    'Artur': [1]
}

# dict.items retorna uma tupla contendo a chave na primeira posição e o valor na segunda posição
for aluno, notas in notas_alunos.items():
    # Casamento de padrão com chave, valor
    match aluno, notas:
        case aluno,[x, y, z]:
            print(f'Aluno {aluno} fez três provas. Média = {(x + y + z)/3:.1f}')

        case aluno,[x, y]:   
            print(f'Aluno {aluno} fez duas provas. Média = {(x + y)/2:.1f}')

        case aluno,[x]:   
            print(f'Aluno {aluno} fez uma prova. Média = {x:.1f}')

        case aluno,[]:   
            print(f'Aluno {aluno} não fez nenhuma prova. REPROVADO')

        case _:
            print('>>> Formato inválido')