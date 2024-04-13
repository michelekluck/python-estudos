# Crie um programa que cadastre os funcionários de uma empresa e seus dependentes. O funcionário deve ser cadastrado com matrícula, nome e dependentes. Os dependentes devem ser inseridos dinamicamente em uma tupla. Dica: use o operador “+=”.

funcionarios_dependentes = []
while True:
    funcionario = input("Digite o nome do funcionário: ")
    matricula = input("Digite a matŕicula do funcionário: ")
    dependentes = tuple()
    dependente = input("DIgite o nome do dependente (0 para sair): ")
    if dependente == "0":
        break
    dependentes += (dependente,)
    funcionario = (funcionario, matricula, dependentes)
    
    funcionarios_dependentes.append(funcionario)
    if input("Gostaria de cadastrar mais um funcionário: (s/n): ") == "n":
        break
print(funcionarios_dependentes)
