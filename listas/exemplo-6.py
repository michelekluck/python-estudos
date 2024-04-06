notas = [] # criamos uma lista vazia chamada notas.
for _ in range(7): 
    nota = float(input("Entre com uma das notas: "))
    notas.append(nota) # Cada nota é adicionada à lista notas.
menor = min(notas) # encontramos a função mais baixo (menor)
if notas.count(menor) == 1: # se a nota mais baixa aparece uma vez na lista
    notas.remove(menor) #removemos o menor valor
else: # se nao
    indice = -1 
    for i in range(len(notas)): # encontramos a primeira ocorrencia da nota mais baixa
        if notas[i] == menor:
            indice = i
            break
    notas.pop(indice) # removemos usando o metodo pop
maior = max(notas) # fazemos a mesma coisa para encontrar a nota mais alta
if notas.count(maior) == 1:
    notas.remove(maior) # removemos da lista
else:
    indice = -1
    for i in range(len(notas)):
        if notas[i] == maior:
            indice = i
            break
    notas.pop(indice)
soma = sum(notas) #somamos todas as notas da lista
print(f"A pontuação final do salto foi {soma:.1f}") #imprimos a pontuação
