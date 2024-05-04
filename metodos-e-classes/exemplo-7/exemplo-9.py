#  Elabore uma classe que simule um dado de jogo. No construtor, deve-se informar quantas faces possui o dado. Caso o valor informado seja inválido, o dado será padrão, de seis faces. Deve ter um método privado de calcular a jogada e um método público de retorno do valor do dado para o usuário. Ao final, deve testar a classe e todos os seus métodos.

import random # o modulo 'random' é usado para gerar numeros aleatorios

class Dado: # definimos uma clase chamada 'Dado'
    def __init__(self, faces=6): # inicialização da classe 'Dado', ele é chamado automaticamente quando uma instancia é criada; recebe o argumento 'faces' que determina quantas faces o dado terá; se nenhum valor for fornecido, o dado terá 6 faces por padrão
        self.__faces = faces if faces > 2 else 6 # inicializamos o atributo de instancia '__faces'; se o valor passado for maior que 2 '__faces' recebe esse valor, caso contrario, recebe 6
        
    def valor_jogada(self): # esse metodo retorna o valor resultante de uma jogada do dado
        return self.__calcular_jogada() # aqui chamamos um metodo interno '__cacular_jogada()' que gera um numero aleatorio entre 1 e o numero de faces do lado

    def __calcular_jogada(self): # esse é um metodo privado que é utilizado internamente na classe para calcular o valor de uma jogada de dado
        return random.randint(1, self.__faces) # utilizamos a função 'randint' do modulo 'random' para gerar um numero aleatorio entre 1 e o numero de faces do lado ('self.__faces)
    
if __name__ == '__main__': # verificamos se o escript esta sendo executado como o programa principal, se for o caso, o codigo dentro do bloco sera executado
    dado4 =  Dado(4) # aqui criamos uma instancia da classe 'Dado' com 4 faces
    print(dado4.valor_jogada()) # chamamos o metodo 'valor_jogada()' da instancia 'dado4' para imprimir o valor resultante de uma jogada
    dado = Dado(1) #  tentamos criar uma instância da classe Dado com apenas 1 face. Como o código na inicialização do objeto verifica se o número de faces é maior que 2, o valor padrão de 6 será usado
    print(dado.valor_jogada()) # Chamamos o método valor_jogada() da instância dado para imprimir o valor resultante de uma jogada
    