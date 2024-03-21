import random
# retorna um numero aletoria entre um determinada faixa (range)
# 0 a 9
# podemos utilizar tanto numeros positivos quanto negativos
# ou apenas um unico paramtero
# (10) = 0 ate 9
# step: 2 = pula de 2 em 2, do 0 ate o 9
num = random.randrange(0,10, 2)
print(num)