agenda = {
    "Maria": "(41) 98765-4321", 
    "João": "(11)  12345-6789",
    "Rosana": "(21) 91827-3645"  
}
print(agenda)

# adiciona um novo elemento no vetor
agenda["José"] = "(19) 98877-1122"
print(agenda) #{'Maria': '(41) 98765-4321', 'João': '(11)  12345-6789', 'Rosana': '(21) 91827-3645', 'José': '(19) 98877-1122'}

# cria um dicionário com chaves e valores específicos
chaves = ["chave1", "chave2", "chave3"]
valores = "valor"
novo_dicionario = dict.fromkeys(chaves, valores)
print(novo_dicionario) #{'chave1': 'valor', 'chave2': 'valor', 'chave3': 'valor'}

# mostra a lista de itens do dicionário
print(agenda.items()) #([('Maria', '(41) 98765-4321'), ('João', '(11)  12345-6789'), ('Rosana', '(21) 91827-3645'), ('José', '(19) 98877-1122')])

# mostra a lista de chaves do dicionário
print(agenda.keys()) #(['Maria', 'João', 'Rosana', 'José'])

# mostra a lista de valores do dicionário
print(agenda.values()) #(['(41) 98765-4321', '(11)  12345-6789', '(21) 91827-3645', '(19) 98877-1122'])

# remove um item de chave específica
agenda.pop("Maria")
print(agenda) #{'João': '(11)  12345-6789', 'Rosana': '(21) 91827-3645', 'José': '(19) 98877-1122'}

# remove o último item inserido
agenda.popitem()
print(agenda) #{'João': '(11)  12345-6789', 'Rosana': '(21) 91827-3645'}

# retorna ou insere o valor de uma chave em específico
print(agenda.setdefault("Rosana", "(21) 91827-3645"))
print(agenda.setdefault("Maria", "(41) 98765-4321"))
print(agenda) #{'João': '(11)  12345-6789', 'Rosana': '(21) 91827-3645', 'Maria': '(41) 98765-4321'}

# adiciona o conteúdo de um dicionário a outro
agenda.update(novo_dicionario)
print(agenda) #{'João': '(11)  12345-6789', 'Rosana': '(21) 91827-3645', 'chave1': 'valor', 'chave2': 'valor', 'chave3': 'valor'}

# limpa o conteúdo de um dicionário
agenda.clear()
print(agenda) #{}