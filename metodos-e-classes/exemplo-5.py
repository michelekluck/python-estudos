# Escopo de acesso em classes

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        
    def alterar_dados(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        
    def imprimir(self):
        print(f"Cliente:", self.__nome, "- CPF:", self.__cpf)
        
# Dessa forma, uma chamada ao parametro cpf ou mesmo a monenclatura de escopo privado __cpf vão gerar um erro de AttributeError na execução

cliente = Cliente("João", "123.345.344-77")
print(cliente.__cpf)