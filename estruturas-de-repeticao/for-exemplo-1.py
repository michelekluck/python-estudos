# solicita ao usuario um valor inteiro
numero = int(input("Digite um valor."))
# o loop for itera sobre os numeros 1 a 1000
# 'i' assume os valores de 1 a 1000 em cada iteração
for i in range(1, 1001):
    # para cada 'i' no intervalo de 1 a 1000
    # este comando vai imprimir a soma do numero fornecido pelo usuario (numero) com o valor atual de 'i'
    print(numero + i)

""" 
O codigo produzira a seguinte saida:
para cada numero de 1 a 1000, será imperessa
a soma desse numero com o numero fornecido pelo usuario
Isso resultará em uma serie de numeros que consiste
na sequencia de 'numero + 1', 'numero + 2', 'numero + 3',
.... 'numero + 1000'.
"""