# Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda, exibindo, ao final, o dicionário.

agenda = {} #criamos um dicionario vazio
print("*** Cadastro de telefones ***")
while True: #laço de repetição infinito, so sera interrompido quando o usuario decidir
    contato = input("Digite o nome do contato: ") #guardamos a info que o usuario digitar em contato
    telefone =  input("Digite o telefone do contato: ") #mesma coisa em telefone
    agenda[contato] = telefone # adicionamos o telefone no dicionario agenda. A chave para encontrarmos o telefone será contato.
    if input ("Deseja cadastrar um novo contato (s/n) ") == "n": #se o usuario digitar n o laço é interrompido
        break 
print(agenda) # mostra o dicioario agenda com todos os contato e seus respectivos numeros q foram cadastrados