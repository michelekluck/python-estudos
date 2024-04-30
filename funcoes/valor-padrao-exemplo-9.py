agenda_telefonica = {}# cria um dicionario

def inserir(nome, agenda, telefone = "Sem telefone"):
    if nome in agenda:
        if input("Contato já cadastrado. Deseja alterar o telefone? (s/n)") == "n":
            return False
    agenda[nome] = telefone
    return True

inserir("Fulano", agenda_telefonica) 
inserir("Beltrano", agenda_telefonica, 1223334444)
inserir("Maria", agenda_nao_telefonica)

print(agenda_telefonica)