print("Digite as quatro notas  bimestrais da disciplina: ")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

faltas = int(input("Digite o numero de faltas: "))
# o calcaulo de media é a soma dos valores e o resultado dividio pela quantidade de dados
media = (nota1 + nota2 + nota3 + nota4) / 4
print("Sua media da disciplina foi", media)

# são 40 aulas
presenca = 100 - (faltas * 100) / 40
print("Sua porcentagem de presença é de", presenca, "%")

# 75% é o minimo exigido de presença
# se a media for MAIOR e IGUAL E a presença for MAIOR e IGUAL vai ser APROVADO
if media >= 7 and presenca >= 75:
    print("Você está aprovado na disciplina")
# se a media for maior ou igual a 7 e a presença menor que 75 vai ser reprovado por falta
elif media >= 7 and presenca < 75:
    print("Você foi reprovado por faltas!")
# se a media for menor que 7 e a presença maior que 75 foi reprovado por nota
elif media < 7 and presenca >= 75:
    print("Você foi reprovado por nota!")
else:
# se não foi reprovado por nota e por falta
    print("Você foi reprovado por nota e por faltas")
