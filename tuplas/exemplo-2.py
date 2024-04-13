# Elabore um programa que solicite ao usuário o cadastro de endereços para entrega de produtos de uma loja.

enderecos = [] # criamos uma lista vazia chamada enderecos para armazenar todos os endereços de entrega
print("Cadastro de Endereços de Entrega")
while True: # laço de repetição infinito que so sera interrompido quando o usuario decidir
    logradouro = input("Digite o logradouro: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novo_endereco = (logradouro, numero, bairro, cidade, estado) # criamos uma TUPLA com os detalhes do endereço fornecido
    enderecos.append(novo_endereco) # adicionado a tupla novo_endereco a lista enderecos
    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break
print("Os endereços cadastrados são:")
for i in range(0, len(enderecos)): # iniciamos um laço for que percorre todos os endereços na lista enderecos
        endereco = enderecos[i]
        print(f"{i}. {endereco[0]}, {endereco[1]}, {endereco[2]} - {endereco[3]}/{endereco[4]}") # cada endereço é exibido na tela, mostrando o indice do endereço na lista e seus detalhes