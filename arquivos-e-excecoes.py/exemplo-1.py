# Crie uma aplicação a qual pede o nome do usuário. Em seguida, salve em um arquivo chamado “nome.txt” o nome desta pessoa.

nome = input("Digite seu nome: ")

with open("nome.txt", "w") as f: #abre o arquivo "nome.txt" no modo escrita "w" em uma variavel chamada f
    f.write(nome) #chamamos o metodo write() para escrever o conteudo da variavel nome no arquivo