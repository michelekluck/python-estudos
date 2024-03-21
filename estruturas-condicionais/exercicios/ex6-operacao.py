num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
operacao = input(("Qual operação você deseja fazer ( + - * / )?"))
result = 0
if operacao == '+':
    result = num1 + num2
elif operacao == '-':
    result = num1 - num2
elif operacao == '*':
    result = num1 * num2
elif operacao == '/':
    result = num1 / num2
else:
    operacao = 'erro'
if operacao == 'erro':
    print("Operação invalida")
else:
    print(num1,operacao, num2, "=", result)


