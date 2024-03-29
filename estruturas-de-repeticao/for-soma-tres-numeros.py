# inicializa com a variavel soma igual a 0
# soma vai guardar o valor da soma dos valores digitados pelo usuario
soma = 0 
# loop for itera sobre os numeros de 0 a 2 ( 3 no total )
# a variavel i assume os valores de 0 a 2 em cada iteração
for i in range(3):
    # solicita ao usuario que insira um numero inteiro
    # indica ao usuario qual umero ele está digitando
    # i + 1 é usado para exibir os nuemros de 1 a 3 e não de 0 a 2
    num = int(input("Digite o " + str(i+1) + " número: "))
    # adicionado o numero digitado (num) a soma acumulada (soma)
    # atribui o resultado de volta a variavel soma
    # acumula os 3 numeros fornecidos pelo usuario
    soma += num
# mostra a soma acumulada para o usuario
print("A soma dos números é", soma)