#  Crie um programa que peça ao usuário 5 números inteiros. Salve estes números dentro de um arquivo chamado “números.txt”. Cada número deve ocupar uma linha.

import json

lista_numeros = [] # cria uma lista vazia
for i in range(5): # vai pedir 5 vezes que o usuario digite um numero 
    numero = int(input("Digite um numero inteiro: ")) # armazeno os numeros que o usuario digitou na variavel numero
    lista_numeros.append(numero) # adiciona os numeros digitados pelo usuario na lista_numeros
    
with open("numeros.txt", "w") as arquivo: #abre o arquivo de texto "numeros.txt" em modo escrira "w" como variavel ARQUIVO
    for numero in lista_numeros: # para cada numero na lista de numeros
        arquivo.write(str(numero) + "\n") # vai escrever cada numero da lista dentro do arquivo (numeros.txt)

soma = 0 # cria uma variavel chamada soma que inicia com o numero 0

with open("numeros.txt", "r") as arquivo: # abre o arquivo de texto "numeros.txt" em modo leitura "r" como variavel ARQUIVO
    for linha in arquivo.readlines(): # readlines() le todo o conteudo do arquivo separado linha por linha como strings em uma unica lista
        soma += int(linha) # vai somar linha após linha até chegar ao resultado

print(soma) #vau mostrar na tela o resultado da soma