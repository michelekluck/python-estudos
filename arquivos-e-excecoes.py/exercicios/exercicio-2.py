import json

soma = 0

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo.readlines(): # readlines() le todo o conteudo do arquivo separado linha por linha como strings em uma unica lista
        soma += int(linha)

print(soma)

