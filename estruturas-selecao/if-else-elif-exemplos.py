idade = int(input("Qual é a sua idade? "))

#primeiro bloco de if/else
if idade < 18:
    print("Você é menor de idade!")
else:
    print("Você é maior de idade!")
    

#segundo bloco if/elif/else
media = float(input("Qual é a sua media na disciplina? "))

if media >= 7:
    print("Parabéns, você foi aprovado com a média", media)
    print("Continue estudando e se prepranda para os proximos desafios")
elif media >= 5:
    print("Você está em recuperação com média", media)
    print("Você precisa estudar mais para a proxima vez")
else:
    print("Infelizmente, você foi reprovado com a média", media)
    print("Você precisa estudar maid para a proxima oportunidade")
    
#terceiro bloco de if/else
saldo = float(input("Qual é seu saldo na conta-corrente?"))

if saldo < 0:
    print("O seu saldo está negativo!")
elif saldo == 0:
    print("O seu saldo está zerado!")
else:
    print("O seu saldo está positivo!")