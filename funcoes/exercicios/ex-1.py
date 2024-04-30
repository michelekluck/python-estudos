# Crie um programa que calcule, a partir de uma função, o fatorial de um número. Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Observação: por propriedade, 0! = 1.

def fatorial(numero):
    # segundo as propriedades de fatorial
    if numero == 0: #porque o fatorial de 0 é sempre 1
        return 1
    fat = 1 # inicializa a variavel fat como 1 
    for i in range(numero, 0, -1): # itera de 'numero' até 1, decrementando de 1 em 1
        fat *= i #multiplica o valor de fat pelo valor atual de 'i' em cada iteração do loop, até o 1
    return fat # retorna o resultado do calculo fatorial
numero = int(input("Digite um numero inteiro para calcular seu fatorial: "))
fat = fatorial(numero) #chama a função 'fatorial' com o numero fornecido pelo usuário e armazena o resultado na variavel fat
print(f"O fatorial de {numero} é {fat}")