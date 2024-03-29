# incializa uma variavel chamada fatorial com valor 1
# será usada para armazenar o resultado do calculo fatorial
fatorial = 1
# inicializa uma variavel chamada expressao com uma string
# será usada para construir a expressão do calculo fatorial
expressao = "Expressão: "
# solicita que o usuario digite um numero inteiro
# o numero é atribuido a variavel num
num = int(input("Digite um número para o cálculo do fatorial: "))
# o loop for vai iterar de 'num' até 1 (excluindo o 0), de forma decrescente
for i in range (num, 0, -1):
    # multiplica o valor atual do fatorial  pelo valor atual do iterador ('i')
    # atribui o resultado de volta a variavel fatorial
    # isso calcula o fatorial
    fatorial *= i
    # concatena a string representando o valor atual do iterador (i) a expressao
    # isso é feito p/ construir a expressao do calculo do fatorial
    expressao += str(i)
    # verifica se o valor atual do i é maior que 1
    # se for, concatena a string " * " a expressao
    # isso é feito para construir a expressao do calculo fatorial
    if i > 1:
        expressao += " * "
print("O valor do fatorial de", num, "é", fatorial, expressao)
    