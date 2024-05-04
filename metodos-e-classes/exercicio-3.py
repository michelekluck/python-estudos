# As classes devem apresentar comportamento genérico, uma vez que podemos criar diversos objetos diferentes a partir delas, e cada um com suas próprias informações

class Cliente:
    def definir_dados(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def imprimir(self):
        print(f"Cliente:", self.nome, "- CPF:", self.cpf)
            
cliente = Cliente()
cliente.definir_dados("Maria", "987.654.321-00")
cliente.imprimir()