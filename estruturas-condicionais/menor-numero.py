print("Por favor, insira três números diferentes.")
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

#verificando se os numeros são diferentes
if num1 == num2:
    print("Os numeros inseridos não são diferentes")
elif num1 == num3:
    print("Os numeros inseridos não são diferentes")
elif num2 == num3:
    print("Os numeros inseridos não são diferentes")
else:
    if num1 < num2:
        if num1 < num3:
            print("O menor número é:", num1)
        else:
            print("O menor numero é:", num3)
    elif num2 < num3:
        print("O menor número é:" , num2)
    else:
        print("O menor numero é:", num3)