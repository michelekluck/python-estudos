#  Crie um programa que escreva um arquivo chamado "alunos.txt" contendo informações de alunos (um aluno por linha, separado por vírgulas - nome, idade, nota) conforme a lista abaixo. Dica: se quiser, pesquise sobre a função “map” em Python. Ela serve para substituir o “for” em alguns casos.

import json

# cria a lista aluns
alunos = [
    ("João", 18, 9.5),
    ("Maria", 19, 8.7),
    ("Pedro", 20, 7.2),
    ("Ana", 18, 9.0),
    ("Carlos", 19, 8.5)
]

with open("alunos.txt", "w") as arquivo: #abre o arquivo de texto "alunos.txt" no modo escrita como variavel arquivo
    for aluno in alunos: #para cada aluno na lista alunos
        # map(str,aluno)-> cada tupla 'aluno' é convertida em uma string
        # o join apenas pode unir strings e as tuplas contem diferentes tipos de dados
        # ",".join -> une os elementos da tupla separando-as por virgulas
        # + "\n" adiciona um caractere de nova linha ao final da string
        linha = ",".join(map(str, aluno)) + "\n" 
        arquivo.write(linha) #escrevemos o que esta na variavel linha dentro da variavel arquivo que é nosso arquivo de texto