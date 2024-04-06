listaUm = []
listaDois = []
listaTres = []
for _ in range(5):
    numerosUm = int(input("Digite um dos 5 numeros: "))
    listaUm.append(numerosUm)
for _ in range(5):
    numerosDois = int(input("Digite um dos outros 5 numeros: "))
    listaDois.append(numerosDois)

for i in range(5):
    listaTres.append(listaUm[i])
    listaTres.append(listaDois[i])
print(f"Primeira lista: {listaUm}")
print(f"Segunda lista: {listaDois}")
print(f"Terceira lista, com os numeros juntos intercalados: {listaTres}")
    
