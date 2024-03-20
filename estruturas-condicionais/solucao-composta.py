# solicita as notas do usuário
#solicita as notas do usuario
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

#calcula a media das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("O estudante foi aprovado")
    print("Ainda estamos dentro do if")
else:
    print("O estudante foi reprovado")
    # exibe a media
    print(f"A media do estudante é: {media:.2f}")
