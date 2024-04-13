# Crie um programa que efetue o cadastro de produtos e preços. Caso o produto já exista, deve perguntar se o usuário pretende atualizar o valor. Imprima o dicionário no fim do programa em formato de lista.
lista_produtos= {}
while True:
    produto = input("Insira o nome do produto: ")
    preco = float(input("Insira o preço do produto digitado: "))
    if produto in lista_produtos:
        if input(f"Produto já cadastrado com o valor {lista_produtos[produto]}. Deseja alterar o valor? (s/n)") == "n":
            continue
        lista_produtos[produto] = preco
        if input("Cadastrar um novo produto? (s/n)") == "n":
            break
    for produto in lista_produtos:
        print(f"{produto:>20}: R${lista_produtos[produto]:.2f}")        