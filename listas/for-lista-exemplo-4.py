nums = [17, 33, 23, 11, 8, 15, 9] # cria uma lista nums
maior = nums[0] # variavel maior é inicializada com o primeiro elemento da lista nums
menor = nums[0] # A variável menor é inicializada com o primeiro elemento da lista nums
for num in nums: # para cada elemento em nums
	if num > maior: # se num for maior do que o valor atualmente armazenado na variavel maior
			maior = num # se for verdadeiro, maior é atualizado para esse valor 'num'
	if num < menor: # se o elemento atual de 'num' for menor do que o valor atualmente armazenado na variavel 'menor'
		menor = num #'menor' é atualizado para o valor de 'num'
print("O maior numero da lista é", maior, "e o menor é", menor)

"""esse codigo percorre a lista 'nums' e compara cada elemento com as variaveis 'maior' e 'menor', atualizando-as
conforme o necessário para encontrar o maior e o menor elemento da lista.
"""