nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
media = (nota1 +nota2) / 2

if media >= 7:
    print("Parabéns, você foi aprovado com media", media)
    print("Continue estudando e se preparando para os proximos desafios")
    
elif media >= 5:
    print("Você está em recuperação com média", media)
    print("Você precisa estudar mais para a próxima prova")
else:
    print("Infelizmente, você foi reprovado com media", media)
    print("Você precisa estudar mais para a proxima oportunidade")