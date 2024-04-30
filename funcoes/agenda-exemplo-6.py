agenda_telefonica = {} #dicionario vazio

#essa função atribui o numero de telefone fornecido ao nome do contato no dicioánrio 'agenda'
def inserir(nome, telefone, agenda): # nome telefone e agenda são parametros
    agenda[nome] = telefone
# utiliza o valor do parametro 'nome' como chave para o dicionario 'agenda'
# atribui o valor do parametro 'telefone' como valor correspondente a essa chave
# Isso significa que, quando você quer buscar um contato na agenda, você usa o nome como referência para encontrar o número de telefone associado a esse nome.
while True:
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    inserir(nome, telefone, agenda_telefonica)
    if input("Gostaria de adicionar um nvovo contato? (s/n) ") == 'n':
        break
print(agenda_telefonica)