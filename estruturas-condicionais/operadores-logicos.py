print("Por favor, insira três numeros diferentes: ")
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

# as tres condições inicias verificam se os numeros são iguais
#f foram combinadas em uma unica condição usando o operador or
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Os numeros inseridos não são diferentes")
else:
    #o uso de condições aninhadas foi reduzido ao aplicar o operador and
    if num1 < num2 and num1 < num3:
        print("O menor número é:", num1)
    elif num2 < num3:
        print("O menor numero é:", num2)
    else:
        print("O menor numero é:", num3)