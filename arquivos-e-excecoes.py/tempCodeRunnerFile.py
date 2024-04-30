with open("nome.txt", "r") as f:  #'r' modo leitura
    for linha in f.readlines(): #f.readlines é uma lista de strings, cada string é uma linha do arquivo, usamos for para mostrar cada linha individualmente na tela para o usuario
        print(linha)