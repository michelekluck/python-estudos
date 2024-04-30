#  Crie um programa que peça ao usuário 5 números inteiros. Salve estes números dentro de um arquivo chamado “números.txt”. Cada número deve ocupar uma linha.

lista_numeros = []
for i in range(5):
    numero = int(input("Digite um numero inteiro: "))
    lista_numeros.append(numero)
    
with open("numeros.txt", "w") as arquivo:
    for numero in lista_numeros:
        arquivo.write(str(numero) + "\n")