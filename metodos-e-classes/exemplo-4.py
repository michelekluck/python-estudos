# Construtor de classe
# Construtor: uma chamada obrigatoria na criação o objeto que solicita as informações internas iniciais da classe

class Cliente:
    def init (self,nome,cpf): # init = metodo construtor
        self.nome = nome
        self.cpf = cpf
    
    def alterar_dados(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def imprimir(self):
        print(f"Cliente:", self.nome, "- CPF:", self.cpf)
        
cliente = Cliente("João", "123.456.789-00") # chamada à criação de um objeto da classe Cliente demanda a passagem dos dois valores: nome e cpf
cliente.imprimir()

# Não é permitido a criação de diversos construtores
# É possivel dar valores-padrão para os parametros do construtor:
# def init (self. nome, cpf"000.000.000.00")
# Nesse caso se o valor de cpf não for informado na criação do objeto, o atributo cpf receberá o valor-padrão "000.000.000-00"