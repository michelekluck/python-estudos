nota1 = float(input("digite a nota da primeira prova: "))
nota2 = float(input("digite  a nota da segunda prova: "))
media = (nota1 +nota2) / 2.0

if media >= 7:
    print("Parabéns, você foi aprovado com média", media)
    print("Continue estudando e se preparanda para os proximos desafios")
    
else:
    print("Infelizmente, você foi reprovado com média", media)
    print("Você precisa estudar mais para a próxima oportunidade.")