# Elabore uma classe Quadrado, que receba em seu construtor o lado e tenha como função para seus métodos calcular perímetro, área e diagonal, bem como um método de impressão informando: “Quadrado de lado {lado}”. Ao final, deve testar a classe e todos os seus métodos.

import math # isso importa o modulo de matematica do python, permitindo o uso de funções matematicas como "sqrt"(raiz quadrada)

class Quadrado: # criação da classe "Quadrado"
    def __init__(self, lado): # metodo de inicialização da classe. ele é chamado automaticamente quando uma nova instancia de classe é criada. recebe o argumento 'lado' que é utilizado para inicializar o atributo '__lado'
        self.__lado = lado if lado >= 0 else 0 # estamos inicializando o atributo de instancia '__lado'. se o valor for maior ou igual a 0, '__lado' recebe o valor, caso contrario recebe 0
    
    def calc_perimetro(self): # esse metodo calcula o perimetro do quadrado. o perimtero de um quadrado é o comprimento de seus quatro lados, que é iguaç ao lado multiplicado por 2
        return self.__lado ** 2
    
    def calc_area(self): # esse metodo calcula a area do quadrado. a area do quadrado é o lado elevado ao quadrado
        return self.__lado ** 2
    
    def calc_diagonal(self): # esse metodo calcula a diagonal do quadrado. a diagonal de um quadrado é o lado multiplicado pela raiz quadrada de 2
        return self.__lado * math.sqrt(2)
    # math.sqrt calcula a raiz quadrada
    
    def imprimir(self): # esse metodo imprime uma mensagem indicando o tamanho do lado do quadrado
        print("Quadrado de lado", self.__lado)
        
if __name__ == '__main__': # essa linha verifica se o script está sendo executado como o programa inicial. se for o caso, o codigo dentrio desse bloco será executado
    quadrado = Quadrado(5) # uma instancia da classe 'Quadrado' é criada com um lado de comprimento 5
    quadrado.imprimir() # esse metodo é chamado para imprimir uma mensagem indicando o tamanho do lado do quadrado
    print("Perímetro:", quadrado. calc_perimetro()) # esse print chama o metodo 'calc_perimetro()' da instancia 'quadrado' para calcular e imprimir o perimetro do quadrado
    print("Área:", quadrado.calc_area()) # esse print chama o metodo 'calc_area()' da instancia 'quadrado' para calcular e imprimir a area do quadrado
    print(f"Diagonal: {quadrado.calc_diagonal():.2f}") # esse print chama o metodo 'calc_diagonal()' da instancia 'quadrado' para calcular a diagonal do quadrado, e a formata como string com duas casas decimais       
        