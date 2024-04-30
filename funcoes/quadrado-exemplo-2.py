def quadrado(numero): #criando uma função chamada quadrado
    resultado = numero ** 2 # ** calcula potencia
    return resultado
for i in range(21):
    print(f"{i} * {i} = {quadrado(i)}")