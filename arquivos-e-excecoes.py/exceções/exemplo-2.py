# Adicione um tratamento de exceções para um algoritmo que pede ao usuário para que ele(a) digite um número e, em seguida, dividisse aquele número por zero

numero = int(input("Digite um número: "))
try: # linhas de codigo que podem dar erro
    print(numero/0.0)
except: # codigo a ser executado caso o que estiver dentro de try não funcionar
    print("Não foi possível dividir o número por 0")