# Crie um programa que efetue o cadastro de pessoas com nome, RG e CPF por meio de tuplas, adicionando-as a uma lista e imprimindo essa lista no fim do programa.

dados_pessoais = []
print("Cadastro")
while True:
    nome = str(input("Digite o nome: "))
    rg = input("Digite o RG: ")
    cpf = input("Digite o CPF: ")
    novo_cadastro = (nome, rg, cpf)
    dados_pessoais.append(novo_cadastro)
    if input("Deseja cadastrar uma nova pessoa: (s/n)") == "n":
        break
print("Os dados cadastrados são:")
for i in range(0, len(dados_pessoais)):
    dados = dados_pessoais[i]
print(dados_pessoais)

