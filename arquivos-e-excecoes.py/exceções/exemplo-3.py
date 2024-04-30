# Mostre um menu simples com opções numéricas ao usuário. Converta a opção digitada para um número inteiro. Mostre uma mensagem simples de erro se o valor digitado for inválido (como um texto)

while True:
    print("1. Doces")
    print("2. Salgados")
    print("3. Bebidas")
    print("4. Sair")
    
    try: 
        opcao = int(input("Digite uma opção: "))
    except:
        print("Você digitou uma opção inválida. Tente novamente")
        continue
        
    if opcao >= 1 and opcao <= 3:
        print(f"Você digitou uma opção vaĺida \"{opcao}\".")
    elif opcao == 4:
        break
    else:
        print("Você digitou uma opção inválida. Tente novamente.")
    