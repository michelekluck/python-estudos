# O acesso aos dados deve ser feito a partir de métodos publicos de classe

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        if self.__cpf_valido(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = cpf
    
    def imprimir(self):
        print(f"Cliente:", self.__nome, "- CPF:", self.__cpf)
        
    def mudar_cpf(self, cpf):
        if self.__cpf_valido(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = "CPF Inválido"
            
    def ler_cpf(self):
        return self.__cpf
            
    def __cpf_valido(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False
        
cliente = Cliente("João", "88485934403")
print(cliente.ler_cpf())
cliente.mudar_cpf("777384")
print(cliente.ler_cpf())

# Os atributos da classe são privados, eles não devem ser acessados diretamente de fora da classe
# Isso garante que a classe tenha controle total sobre aseus dados e possa realizar validações internas, se necessário
# O metodo __cpf_valido() também é privado
# Para tonar um metodo privado, basta adicuionar dois underscores antes de seu nome
