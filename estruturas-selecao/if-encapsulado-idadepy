# if dentro de outro if
# condições mais restritivas em primeiro lugar, criando uma hierarquia lógica na execução
# condições mais simples são verificadas primeiro
# evitando execução desnecessaria de outras condições

idade = int(input("Qual a sua idade? "))

# verifica se possui 18 anos ou mais
if idade >= 18:
    # se sim mostrará:
    print("Você é maior de idade")
    # se tiver 21 anos ou mais
    # colocamos dentro de outro if porque quem tem 21 anos obviamente tem mais de 18
    if idade >= 21:
        print("Você pode beber nos Estados Unidos")
else:
    # se tem menos que 18 anos
    print("Você é menor de idade")
    
# usar if dentro de if torna o codigo mais dificil de ler e entender
# pode ser melhorado com uso de operadores logicos
# da pra usar if dentro de if dentro de if mas não é recomendado