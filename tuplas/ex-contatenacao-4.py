# Elabore um programa que concatene tuplas.

endereco_puc = (
    "Rua Imaculada Conceição",
    "1555",
    "Prado Velho",
    "Curitiba",
    "PR"      
)
print(id(endereco_puc))
endereco_puc += ("Brazil",) # uma tupla com um unico dado deve ser declarada com uma virgula
print(endereco_puc)
print(id(endereco_puc))

# foi criado uma nova tupla, e esta foi atribuida a variavel endereco_puc