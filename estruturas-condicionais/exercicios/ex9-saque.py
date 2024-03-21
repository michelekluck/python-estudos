valor = int(input("Qual valor deseja sacar?"))
resto = valor

#inicia numero de notas em zero
# n = notas
n1 = n5 = n10 = n50 = n100 = 0

# se o valor (digitado) for enor ou maior que 600 vai dar erro
if valor < 10 or valor > 600:
    print("Saque menor que o valor minimo ou excede o valor maximo")
# se nao
else:
    # se resto (valor) for maior ou igual a 100
    if resto >= 100:
        sobra = resto % 100
        n100 = int((resto - sobra) / 100)
        resto = sobra
    if resto >= 50:
        sobra = resto % 50
        n50 = int((resto - sobra) / 50)
        resto = sobra
    if resto >= 10:
        sobra = resto % 10
        n10 = int((resto - sobra) / 10 )
        resto = sobra
    if resto >= 5:
        sobra = resto % 5
        n5 = int((resto - sobra) / 5)
        resto = sobra

    n1 = resto
    print("Notas de 100:", n100)
    print("Notas de 50:", n50)
    print("Notas de 10:", n10)
    print("Notas de 5:", n5)
    print("Notas de 1:", n1)