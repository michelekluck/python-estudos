# Usando o exemplo de aplicação 1, leia o nome salvo no arquivo “nome.txt”, mostrando cada caractere em uma linha separada.

with open("nome.txt", "r") as f: # 'r' significa que estamos abrindo o arquivo 'nome.txt' no modo leitura
    conteudo = f.read() # o conteudo do arquivo é lido e armazenado na variavel conteudo
    
    for letra in conteudo: #usamos um for para mostrar cada letra dentro de uma unica linha
        print(letra)