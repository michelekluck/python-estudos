# Elabore um programa que use uma função chamada somar(), que efetua a soma de uma quantidade aleatória de números informados, retornando o resultado da operação.

def somar(*numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma

resultado = somar (2, 3, 4, 5, 8)
print(f"A soma dos numeros é {resultado}")