agenda_telefonica = {}

def inserir(nome, telefone, agenda):
    if nome in agenda: #verifica se o nome do contato ja está na agenda
        if input("Contato ja cadastrado. Deseja alterar o telefone? (s/n) ") == "n": # se estiver, pergunta ao usuario se ele deseja alterar o telefone do contato
            return False # se o usuario optar por nao alterar, a função retorna false
    agenda[nome] = telefone # se o contato ainda nao existe na agenda/ou o usuario quiser atualizar, esse trechp adiciona o novo contato
    return True #após adicionar/atualizar o contato, a função retorna true -> isso indica que a operação de adicionar/atualizar o contato foi bem sucedida
while True: # enquanto a condição for verdadeira, o loop continuará, a menos que seha interrompido por um break
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    if inserir(nome, telefone, agenda_telefonica): #chama a função 'inserir', se a função for true, significa que o contato ja foi adicionado
        print("Contato adicionado ou atualizado com sucesso!")
    else:
        print("Falha ao tentar adicionar o contato!") # caso contrario, a mensagem de erro aparecerá
    if input("Gostaria de adicionar um novo contato? (s/n)") == "n":
        break
print(agenda_telefonica)