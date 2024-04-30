# Salve dois números decimais em novas linhas do mesmo arquivo “nome.txt”.
primeiro_numero = 1.01
segundo_numero = -2.95

with open("nome.txt", "a") as f: #'a' indica que estamos acrescentandp dados em um arquivo sem apagar o que já tinhamos armazenado antes
    #write() servem para que armazenemos os dois numeros no arquivo
    f.write("\n"+str(primeiro_numero)) #str() convertemos os numeros para string
    #\n serve para que salvemos cada numero em uma linha separada
    f.write("\n"+str(segundo_numero))