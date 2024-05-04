class Cliente:
 
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
 
    def alterar_dados(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
 
    def imprimir(self):
        print(f"Cliente:", self.__nome, "- CPF:", self.__cpf)

cliente = Cliente("João", "123.456.789-00")
print(cliente.__cpf)