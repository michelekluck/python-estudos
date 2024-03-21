"""lado1 = int(input("Tamanho do primeiro lado: "))
lado2 = int(input("Tamanho do segundo lado: "))
lado3 = int(input("Tamanho do terceiro lado: "))

if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
    print("É um Triangulo!")
elif lado1 == lado2 == lado3:
    print("É um equilátero!")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("É um isósceles!")
elif lado1 != lado2 != lado3:
    print("É um escaleno!")
else:
    print("Valor invalido") """

print ("Informe os três lados de um triangulo: ")
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 + lado2 < lado3 or lado2 + lado2 < lado1 or lado3 + lado1 < lado2:
    print("Estes lados não formam um triangulo")
else:
    if lado1 == lado2 and lado1 == lado3:
        print("É um triangulo equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("É um triangulo isosceles.")
    else:
        print("É um triangulo escaleno")
