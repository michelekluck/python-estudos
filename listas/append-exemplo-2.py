pares = [ ] # lista que vai armazenar os numeros pares
impares = [ ] # lista que vai armazenar os numeros impares
for i in range(5): # laço que vai se repetir 5 vezes (o a 4)
	num = int(input("Digite um numero: "))
	if num % 2 == 0: #um numero é par se o resto da divisão por 2 for igual a 0
		pares.append(num) # se a condição for true, adicionamos num a lista pares
	else: # se for false (num for impar) 
		impares.append(num) #adicionamos a lista impares
print("Numeros pares:", pares, "Numeros impares:" ,impares)