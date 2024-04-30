import json

def escrever(data,arquivo):
    with open(arquivo+ '.json', 'w') as f:
        json.dump(data, f)
        f.close
    
def ler(arquivo):
    dados = {}
    try:
        with open(arquivo+'.json', 'r') as f:
            dados = json.load(f)
            f.close()
            return dados
    except FileNotFoundError:
        print("Arquivo não encontrado")

dicionario=[{"Nome": "Mario", "Sobrenome": "Silva"}, 
            {"Nome": "Maria", "Sobrenome": "Ferreira" }]   
escrever(dicionario, "pessoas")
dadosRetornados = ler("pessoas")

print(dadosRetornados)