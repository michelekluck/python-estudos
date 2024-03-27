nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
media = (nota1 +nota2) / 2

if media >= 9.5:
    print("Parabéns, a sua nota foi excelente! Você foi aprovado com a me´dia", media)
elif media >= 8:
    print("Parabéns, a sua nota foi muito boa! Você foi aprovado com a média", media)
elif media >= 7:
    print("Parabéns, você foi aprovado com média", media)
    print("Continue estudandando e se preparando para os proximos desafios")
elif media >= 5:
    print("Você está em recuperação com média", media)
    print("Você precisa estudar mais para a próxima prova")
else:
    print("Infelizmente, você foi reprovado com media", media)
    print("Você precisa estudar mais para a proxima oportunidade")   