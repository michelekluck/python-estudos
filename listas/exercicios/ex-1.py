listaNumeros = []
for i in range(6):
    numeros = int(input("Digite um numero: "))
    listaNumeros.append(numeros)
soma = sum(listaNumeros)
media = soma / 6
print(f"media = {media}")
resultadoMaior = []
resultadoMenor = []
for i in range(len(listaNumeros)):
    if listaNumeros[i] >= media:
        resultadoMaior.append(listaNumeros[i])
    else:
        resultadoMenor.append(listaNumeros[i])
print(f"Numeros iguais ou/e acima da media: {resultadoMaior}")
print(f"Numeros abaixo da media: {resultadoMenor}")
        

