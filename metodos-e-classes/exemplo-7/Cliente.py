
# Trabalhando com classes em módulos diferentes

class Cliente:
 
    def __init__(self, nome, cpf):
        self.__nome = nome
        if self.__cpf_valido(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = "CPF inválido"
 
    def imprimir(self):
        print(f"Cliente:", self.__nome, "- CPF:", self.__cpf)
 
    def mudar_cpf(self, cpf):
        if self.__cpf_valido(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = "CPF inválido"
 
    def ler_cpf(self):
        return self.__cpf
 
    def __cpf_valido(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False
if __name__ == '__main__':
    # essas linhas só serão executadas caso o arquivo Cliente.py seja executado diretamente
    cliente = Cliente("Maria", "111111111111")
    cliente.imprimir()